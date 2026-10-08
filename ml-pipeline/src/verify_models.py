"""
Verification script for LSTMAtU-Net, TransAtU-Net, ECSA, Loss Functions, and Metrics.
"""

import torch
import numpy as np
from ecsa import ECSAModule
from lstmatu_net import LSTMAtUNet
from transformer_nowcast import TransAtUNet
from loss import BasePaperTLoss, EnhancedWeightedNowcastLoss
from metrics import evaluate_precipitation_metrics


def test_all():
    print("=== 1. Testing ECSA Module ===")
    x_test = torch.randn(2, 64, 32, 32)
    ecsa = ECSAModule(channels=64, spatial_scale=8)
    ecsa_out = ecsa(x_test)
    print(f"ECSA Input shape: {x_test.shape} -> Output shape: {ecsa_out.shape}")
    assert ecsa_out.shape == x_test.shape, "Shape mismatch in ECSA!"

    print("\n=== 2. Testing Base Paper TLoss ===")
    y_pred = torch.tensor([[[[0.1, 0.6], [0.02, 1.2]]]], requires_grad=True)
    y_true = torch.tensor([[[[0.0, 0.8], [0.01, 1.5]]]])
    tloss_fn = BasePaperTLoss()
    loss_val = tloss_fn(y_pred, y_true)
    loss_val.backward()
    print(f"Base TLoss: {loss_val.item():.4f}, Grad computed successfully: {y_pred.grad is not None}")

    print("\n=== 3. Testing Enhanced Weighted Nowcast Loss ===")
    enh_loss_fn = EnhancedWeightedNowcastLoss()
    enh_loss_val = enh_loss_fn(y_pred, y_true)
    print(f"Enhanced Loss: {enh_loss_val.item():.4f}")

    print("\n=== 4. Testing Meteorological Metrics ===")
    pred_np = np.array([0.02, 0.1, 0.4, 0.8, 1.5, 0.0])
    true_np = np.array([0.01, 0.05, 0.6, 0.7, 0.2, 0.0])
    metrics = evaluate_precipitation_metrics(pred_np, true_np, thresholds=(0.05, 0.2, 0.5))
    print("MAE:", metrics["continuous"]["MAE"], "RMSE:", metrics["continuous"]["RMSE"])
    for k, v in metrics["thresholds"].items():
        print(f"  {k} -> CSI: {v['CSI']:.3f}, POD: {v['POD']:.3f}, FAR: {v['FAR']:.3f}")

    print("\n=== 5. Testing Base Paper LSTMAtU-Net Forward Pass ===")
    # Input: Batch=2, Channels=10 (e.g. 5 past timesteps x 2 features), H=64, W=64
    x_grid = torch.randn(2, 10, 64, 64)
    model_lstm = LSTMAtUNet(in_channels=10, out_channels=10, base_c=16)
    out_lstm = model_lstm(x_grid)
    print(f"LSTMAtU-Net Input: {x_grid.shape} -> Output: {out_lstm.shape}")
    assert out_lstm.shape == (2, 10, 64, 64)

    print("\n=== 6. Testing Transformer-Enhanced TransAtU-Net Forward Pass ===")
    model_trans = TransAtUNet(in_channels=10, out_channels=10, base_c=16, num_transformer_layers=2, num_heads=4)
    out_trans = model_trans(x_grid)
    print(f"TransAtU-Net Input: {x_grid.shape} -> Output: {out_trans.shape}")
    assert out_trans.shape == (2, 10, 64, 64)

    print("\n>>> ALL TESTS PASSED SUCCESSFULLY! <<<")


if __name__ == "__main__":
    test_all()
