"""
Efficient Channel and Space Attention (ECSA) Module
Reference: "LSTMAtU-Net: A Precipitation Nowcasting Model Based on ECSA Module" (Sensors 2023, 23, 5785)

The ECSA module preserves spatial structure while adaptively weighting channel dependencies.
Unlike standard ECA which uses Global Average Pooling (GAP) collapsing spatial dimensions to 1x1,
ECSA uses multi-scale Adaptive Average Pooling (AAP) with scale R x R (e.g. 16, 8, 4, 2, 1)
adapted to the feature map resolution at each level of the U-Net.
"""

import torch
import torch.nn as nn


class ECSAModule(nn.Module):
    """
    Efficient Channel and Space Attention (ECSA) Module.
    
    Formula:
        X_tilde = sigma(C1D_3(AAP(X, R))) * X
    
    Args:
        channels (int): Number of input/output channels.
        spatial_scale (int): Target pooling resolution R (e.g., 16, 8, 4, 2, 1).
        kernel_size (int): 1D convolution kernel size across channels (default: 3).
    """
    def __init__(self, channels: int, spatial_scale: int = 4, kernel_size: int = 3):
        super().__init__()
        self.spatial_scale = spatial_scale
        self.aap = nn.AdaptiveAvgPool2d((spatial_scale, spatial_scale))
        
        # 1D convolution along the channel dimension (kernel_size=3 as determined in paper)
        self.conv1d = nn.Conv1d(
            in_channels=1,
            out_channels=1,
            kernel_size=kernel_size,
            padding=(kernel_size - 1) // 2,
            bias=False
        )
        self.sigmoid = nn.Sigmoid()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: Input tensor of shape (B, C, H, W)
        Returns:
            Channel-and-space weighted tensor of shape (B, C, H, W)
        """
        b, c, h, w = x.shape
        
        # 1. Multi-scale Adaptive Average Pooling -> (B, C, R, R)
        pooled = self.aap(x)
        
        # 2. Compress spatial dimension along R*R to form channel summary -> (B, C)
        # Average across the R x R grid to get channel descriptor
        channel_desc = pooled.mean(dim=(-2, -1))  # (B, C)
        
        # 3. 1D Convolution over channel dimension -> (B, 1, C)
        ch_in = channel_desc.unsqueeze(1)         # (B, 1, C)
        ch_weight = self.conv1d(ch_in)             # (B, 1, C)
        ch_weight = self.sigmoid(ch_weight)       # (B, 1, C)
        
        # 4. Reshape to broadcast with x -> (B, C, 1, 1)
        scale = ch_weight.squeeze(1).unsqueeze(-1).unsqueeze(-1)  # (B, C, 1, 1)
        
        return x * scale
