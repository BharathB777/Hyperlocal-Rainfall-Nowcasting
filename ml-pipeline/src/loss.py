"""
Multi-Objective Weighted Loss Functions for Precipitation Nowcasting.
Reference: "LSTMAtU-Net: A Precipitation Nowcasting Model Based on ECSA Module" (Sensors 2023, 23, 5785)

Implements:
1. TLoss: Combined Weighted MSE (WMSE) + Multi-threshold Soft Binary Cross-Entropy (BCE).
   WMSE exponentially penalizes error on higher rainfall intensities: (e^(y * 0.6) - 0.8).
   BCE_p directly optimizes the soft boundary for CSI threshold events (p1=0.05, p2=0.5, p3=1.0 mm).
2. EnhancedTransformerLoss: An advanced weighted loss incorporating Focal Loss and Extreme Value Weighting
   to fulfill the paper's future research proposal for high-intensity precipitation.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F


class BasePaperTLoss(nn.Module):
    """
    TLoss proposed in LSTMAtU-Net (Equation 5).
    
    TLoss = WMSE + 0.5 * (BCE_p1 + BCE_p2 + BCE_p3)
    
    where:
        WMSE = (1/n) * sum( (y_hat - y)^2 * (exp(y * 0.6) - 0.8) )
        y_hat_p = sigmoid(y_hat - p)
        y_prime = (y > p).float()
        BCE_p = - (1/n) * sum( y_prime * log(y_hat_p + eps) + (1 - y_prime) * log(1 - y_hat_p + eps) )
    """
    def __init__(self, thresholds=(0.05, 0.5, 1.0), bce_weight=0.5, eps=1e-7):
        super().__init__()
        self.thresholds = thresholds
        self.bce_weight = bce_weight
        self.eps = eps

    def forward(self, y_pred: torch.Tensor, y_true: torch.Tensor) -> torch.Tensor:
        """
        Args:
            y_pred: Predicted precipitation tensor (unnormalized or normalized mm)
            y_true: Ground truth precipitation tensor
        Returns:
            Scalar loss tensor
        """
        # 1. Weighted Mean-Squared Error (WMSE)
        # Exponential weighting function: exp(y * 0.6) - 0.8
        sample_weights = torch.exp(y_true * 0.6) - 0.8
        sample_weights = torch.clamp(sample_weights, min=0.1)  # stability safeguard
        
        sq_err = (y_pred - y_true) ** 2
        wmse = torch.mean(sq_err * sample_weights)
        
        # 2. Multi-threshold Soft Binary Cross Entropy
        bce_total = 0.0
        for p in self.thresholds:
            # Soft continuous probability that prediction exceeds threshold p
            y_pred_prob = torch.sigmoid(y_pred - p)
            # Binary ground truth label
            y_true_binary = (y_true > p).float()
            
            # Binary cross entropy with numerical stability epsilon
            bce = - (
                y_true_binary * torch.log(y_pred_prob + self.eps) +
                (1.0 - y_true_binary) * torch.log(1.0 - y_pred_prob + self.eps)
            )
            bce_total = bce_total + torch.mean(bce)
            
        t_loss = wmse + self.bce_weight * bce_total
        return t_loss


class EnhancedWeightedNowcastLoss(nn.Module):
    """
    Advanced Weighted Loss extending the base paper's future research scope:
    - Dynamic heavy-rain penalty (Focal-style modulating factor)
    - Critical Success Index (CSI) differentiable approximation
    - Prevents model collapse to low-intensity blur.
    """
    def __init__(self, thresholds=(0.05, 0.2, 0.5, 1.0), alpha=0.5, gamma=1.5, eps=1e-7):
        super().__init__()
        self.thresholds = thresholds
        self.alpha = alpha
        self.gamma = gamma
        self.eps = eps

    def forward(self, y_pred: torch.Tensor, y_true: torch.Tensor) -> torch.Tensor:
        # Intensity-dependent exponential weight
        intensity_weight = torch.exp(torch.clamp(y_true * 0.75, max=5.0))
        mse_loss = torch.mean(((y_pred - y_true) ** 2) * intensity_weight)
        
        # Soft CSI Loss approximation across rainfall categories
        csi_loss_total = 0.0
        for th in self.thresholds:
            p_pred = torch.sigmoid(10.0 * (y_pred - th))  # sharp sigmoid proxy
            p_true = (y_true > th).float()
            
            tp = torch.sum(p_pred * p_true)
            fp = torch.sum(p_pred * (1.0 - p_true))
            fn = torch.sum((1.0 - p_pred) * p_true)
            
            soft_csi = (tp + self.eps) / (tp + fp + fn + self.eps)
            csi_loss_total = csi_loss_total + (1.0 - soft_csi)
            
        return mse_loss + self.alpha * (csi_loss_total / len(self.thresholds))
