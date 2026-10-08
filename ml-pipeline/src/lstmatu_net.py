"""
LSTMAtU-Net: Precipitation Nowcasting Model Based on ECSA Module
Reference: Sensors 2023, 23, 5785 (MDPI)

Key Innovations:
1. Depthwise-Separable Convolutions (DSC) replacing standard convolutions, cutting params ~42%.
2. Efficient Channel and Space Attention (ECSA) on skip connections preserving multi-scale spatial structure.
3. ConvLSTM with Vertical Flow Direction (ConvLSTM-VF) connecting multi-scale hierarchical representations.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from ecsa import ECSAModule


class DepthwiseSeparableConv(nn.Module):
    """3x3 Depthwise Separable Convolution + BatchNorm + ReLU"""
    def __init__(self, in_channels: int, out_channels: int, kernel_size: int = 3, padding: int = 1):
        super().__init__()
        self.depthwise = nn.Conv2d(
            in_channels, in_channels, kernel_size=kernel_size,
            padding=padding, groups=in_channels, bias=False
        )
        self.pointwise = nn.Conv2d(in_channels, out_channels, kernel_size=1, bias=False)
        self.bn = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU(inplace=True)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.depthwise(x)
        x = self.pointwise(x)
        x = self.bn(x)
        x = self.relu(x)
        return x


class DoubleDSCBlock(nn.Module):
    """Two consecutive (3x3 DSC + BN + ReLU) layers"""
    def __init__(self, in_channels: int, out_channels: int):
        super().__init__()
        self.block = nn.Sequential(
            DepthwiseSeparableConv(in_channels, out_channels),
            DepthwiseSeparableConv(out_channels, out_channels),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.block(x)


class VerticalConvLSTMCell(nn.Module):
    """
    Vertical Flow ConvLSTM Cell (Section 3.2, Eq 3).
    Passes spatial-temporal memory M and hidden state H vertically across network layers l.
    """
    def __init__(self, in_channels: int, hidden_channels: int, kernel_size: int = 3):
        super().__init__()
        self.in_channels = in_channels
        self.hidden_channels = hidden_channels
        padding = (kernel_size - 1) // 2

        # Gate convolutions for input X, hidden H, memory M
        # 4 gates: g (candidate), f (forget), i (input), o (output)
        self.conv_x = nn.Conv2d(in_channels, 4 * hidden_channels, kernel_size, padding=padding, bias=True)
        self.conv_h = nn.Conv2d(hidden_channels, 4 * hidden_channels, kernel_size, padding=padding, bias=False)
        self.conv_m = nn.Conv2d(hidden_channels, 4 * hidden_channels, kernel_size, padding=padding, bias=False)

    def forward(self, x: torch.Tensor, h_prev=None, m_prev=None):
        b, _, height, width = x.shape
        if h_prev is None:
            h_prev = torch.zeros(b, self.hidden_channels, height, width, device=x.device, dtype=x.dtype)
        if m_prev is None:
            m_prev = torch.zeros(b, self.hidden_channels, height, width, device=x.device, dtype=x.dtype)

        # Ensure spatial dimension alignment if passing vertically across layers
        if h_prev.shape[-2:] != (height, width):
            h_prev = F.interpolate(h_prev, size=(height, width), mode="bilinear", align_corners=False)
        if m_prev.shape[-2:] != (height, width):
            m_prev = F.interpolate(m_prev, size=(height, width), mode="bilinear", align_corners=False)

        gates = self.conv_x(x) + self.conv_h(h_prev) + self.conv_m(m_prev)
        g_gate, f_gate, i_gate, o_gate = torch.chunk(gates, 4, dim=1)

        g = torch.tanh(g_gate)
        f = torch.sigmoid(f_gate)
        i = torch.sigmoid(i_gate)
        o = torch.sigmoid(o_gate)

        m_next = f * m_prev + i * g
        h_next = o * torch.tanh(m_next)

        return h_next, m_next


class LSTMAtUNet(nn.Module):
    """
    Complete LSTMAtU-Net Architecture (Figure 2).
    
    Args:
        in_channels: Past observation channels * time steps M (e.g. 10 frames * 2 features = 20)
        out_channels: Forecast channels * time steps N (e.g. 10 frames * 1 rainfall = 10)
        features: Channel list for encoder-decoder levels [64, 128, 256, 512, 1024]
    """
    def __init__(self, in_channels: int = 10, out_channels: int = 10, base_c: int = 32):
        super().__init__()
        
        # Initial projection to base feature space
        self.init_conv = nn.Sequential(
            nn.Conv2d(in_channels, base_c, kernel_size=3, padding=1),
            nn.BatchNorm2d(base_c),
            nn.ReLU(inplace=True),
            DepthwiseSeparableConv(base_c, base_c)
        )
        
        # Multi-scale channel widths
        c1, c2, c3, c4, c5 = base_c, base_c * 2, base_c * 4, base_c * 8, base_c * 16

        # Encoder Levels
        self.enc1 = DoubleDSCBlock(base_c, c1)
        self.pool1 = nn.MaxPool2d(2)
        
        self.enc2 = DoubleDSCBlock(c1, c2)
        self.pool2 = nn.MaxPool2d(2)
        
        self.enc3 = DoubleDSCBlock(c2, c3)
        self.pool3 = nn.MaxPool2d(2)
        
        self.enc4 = DoubleDSCBlock(c3, c4)
        self.pool4 = nn.MaxPool2d(2)
        
        # Bottleneck
        self.bottleneck = DoubleDSCBlock(c4, c5)

        # ECSA Attention Modules for each skip level (R = 16, 8, 4, 2, 1)
        self.ecsa1 = ECSAModule(c1, spatial_scale=16)
        self.ecsa2 = ECSAModule(c2, spatial_scale=8)
        self.ecsa3 = ECSAModule(c3, spatial_scale=4)
        self.ecsa4 = ECSAModule(c4, spatial_scale=2)
        self.ecsa5 = ECSAModule(c5, spatial_scale=1)

        # Vertical Flow ConvLSTM Cells connecting hierarchical levels
        self.v_convlstm = VerticalConvLSTMCell(c5, c5)

        # Decoder Levels (Bilinear upsampling + Concat skip + DoubleDSC)
        self.up4 = nn.Upsample(scale_factor=2, mode="bilinear", align_corners=False)
        self.dec4 = DoubleDSCBlock(c5 + c4, c4)

        self.up3 = nn.Upsample(scale_factor=2, mode="bilinear", align_corners=False)
        self.dec3 = DoubleDSCBlock(c4 + c3, c3)

        self.up2 = nn.Upsample(scale_factor=2, mode="bilinear", align_corners=False)
        self.dec2 = DoubleDSCBlock(c3 + c2, c2)

        self.up1 = nn.Upsample(scale_factor=2, mode="bilinear", align_corners=False)
        self.dec1 = DoubleDSCBlock(c2 + c1, c1)

        # Final 1x1 Convolution to generate predicted precipitation frames
        self.final_conv = nn.Conv2d(c1, out_channels, kernel_size=1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: (B, C_in, H, W) e.g., (B, M*channels, H, W)
        Returns:
            y_hat: (B, C_out, H, W) e.g., (B, N*channels, H, W)
        """
        # Encoder
        x0 = self.init_conv(x)
        e1 = self.enc1(x0)
        e2 = self.enc2(self.pool1(e1))
        e3 = self.enc3(self.pool2(e2))
        e4 = self.enc4(self.pool3(e3))
        
        # Bottleneck
        b = self.bottleneck(self.pool4(e4))
        
        # ECSA attention weighting on skip features
        s1 = self.ecsa1(e1)
        s2 = self.ecsa2(e2)
        s3 = self.ecsa3(e3)
        s4 = self.ecsa4(e4)
        sb = self.ecsa5(b)
        
        # Vertical flow ConvLSTM at bottleneck
        h, _ = self.v_convlstm(sb)
        
        # Decoder
        d4 = self.up4(h)
        # Handle odd dimension mismatch if necessary
        if d4.shape[-2:] != s4.shape[-2:]:
            d4 = F.interpolate(d4, size=s4.shape[-2:], mode="bilinear", align_corners=False)
        d4 = self.dec4(torch.cat([d4, s4], dim=1))

        d3 = self.up3(d4)
        if d3.shape[-2:] != s3.shape[-2:]:
            d3 = F.interpolate(d3, size=s3.shape[-2:], mode="bilinear", align_corners=False)
        d3 = self.dec3(torch.cat([d3, s3], dim=1))

        d2 = self.up2(d3)
        if d2.shape[-2:] != s2.shape[-2:]:
            d2 = F.interpolate(d2, size=s2.shape[-2:], mode="bilinear", align_corners=False)
        d2 = self.dec2(torch.cat([d2, s2], dim=1))

        d1 = self.up1(d2)
        if d1.shape[-2:] != s1.shape[-2:]:
            d1 = F.interpolate(d1, size=s1.shape[-2:], mode="bilinear", align_corners=False)
        d1 = self.dec1(torch.cat([d1, s1], dim=1))

        out = self.final_conv(d1)
        return out
