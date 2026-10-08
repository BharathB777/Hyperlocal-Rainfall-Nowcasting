"""
Meteorological Evaluation Metrics for Quantitative Precipitation Nowcasting (QPF).
Reference: Sensors 2023, 23, 5785 (Section 4.2).

Formulas:
- CSI (Critical Success Index / Threat Score): TP / (TP + FP + FN)
- POD (Probability of Detection / Hit Rate):   TP / (TP + FN)
- FAR (False Alarm Rate):                    FP / (TP + FP)
- HSS (Heidke Skill Score):                  2*(TP*TN - FP*FN) / ((TP+FN)*(FN+TN) + (TP+FP)*(FP+TN))
"""

import numpy as np
import torch
from typing import Dict, Union


def compute_contingency_table(y_pred: np.ndarray, y_true: np.ndarray, threshold: float):
    """
    Computes TP, FP, FN, TN for a given rainfall threshold (mm).
    """
    pred_binary = (y_pred >= threshold).astype(bool)
    true_binary = (y_true >= threshold).astype(bool)
    
    tp = np.sum(pred_binary & true_binary)
    fp = np.sum(pred_binary & ~true_binary)
    fn = np.sum(~pred_binary & true_binary)
    tn = np.sum(~pred_binary & ~true_binary)
    
    return tp, fp, fn, tn


def evaluate_precipitation_metrics(
    y_pred: Union[np.ndarray, torch.Tensor],
    y_true: Union[np.ndarray, torch.Tensor],
    thresholds: tuple = (0.05, 0.2, 0.5, 1.0),
    eps: float = 1e-7
) -> Dict[str, Dict[str, float]]:
    """
    Evaluates CSI, POD, FAR, and continuous regression metrics (MAE, RMSE).
    
    Args:
        y_pred: Predicted rainfall values (in original scale mm)
        y_true: Ground truth rainfall values (in original scale mm)
        thresholds: Rain thresholds in mm/interval (e.g. 0.05 light, 0.2 light-moderate, 0.5 moderate-heavy, 1.0 heavy)
        
    Returns:
        Dictionary of scores per threshold plus overall MAE and RMSE.
    """
    if isinstance(y_pred, torch.Tensor):
        y_pred = y_pred.detach().cpu().numpy()
    if isinstance(y_true, torch.Tensor):
        y_true = y_true.detach().cpu().numpy()
        
    mae = float(np.mean(np.abs(y_pred - y_true)))
    rmse = float(np.sqrt(np.mean((y_pred - y_true) ** 2)))
    
    results = {
        "continuous": {"MAE": mae, "RMSE": rmse},
        "thresholds": {}
    }
    
    for th in thresholds:
        tp, fp, fn, tn = compute_contingency_table(y_pred, y_true, th)
        
        csi = tp / (tp + fp + fn + eps)
        pod = tp / (tp + fn + eps)
        far = fp / (tp + fp + eps)
        
        # Heidke Skill Score (HSS)
        denom = (tp + fn) * (fn + tn) + (tp + fp) * (fp + tn)
        hss = 2.0 * (tp * tn - fp * fn) / (denom + eps)
        
        results["thresholds"][f">= {th}mm"] = {
            "CSI": float(csi),
            "POD": float(pod),
            "FAR": float(far),
            "HSS": float(hss),
            "TP": int(tp),
            "FP": int(fp),
            "FN": int(fn),
            "TN": int(tn),
        }
        
    return results
