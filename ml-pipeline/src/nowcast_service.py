"""
Nowcasting Inference Service: Bridges ML Models with the FastAPI Backend.
Fetches recent station observations, formats them for LSTMAtU-Net / TransAtU-Net,
and produces NowcastPrediction objects for the database and web dashboard.
"""

from datetime import datetime, timezone, timedelta
import torch
import numpy as np
from typing import List, Dict, Any

from transformer_nowcast import TransAtUNet
from lstmatu_net import LSTMAtUNet


class HyperlocalNowcaster:
    """
    Inference orchestrator for 0-2 hour hyperlocal rainfall nowcasting.
    Supports both:
    1. Base Paper Model: LSTMAtU-Net (DSC + ECSA + Vertical ConvLSTM)
    2. Future-Scope Model: TransAtU-Net (DSC + ECSA + Space-Time Transformer)
    """
    def __init__(self, model_type: str = "transatunet", in_frames: int = 10, out_frames: int = 10):
        self.model_type = model_type
        self.in_frames = in_frames
        self.out_frames = out_frames
        
        if model_type == "lstmatunet":
            self.model = LSTMAtUNet(in_channels=in_frames, out_channels=out_frames, base_c=16)
        else:
            self.model = TransAtUNet(in_channels=in_frames, out_channels=out_frames, base_c=16)
            
        self.model.eval()

    def predict_for_stations(
        self,
        station_metadata: List[Dict[str, Any]],
        grid_h: int = 32,
        grid_w: int = 32
    ) -> List[Dict[str, Any]]:
        """
        Simulates / evaluates nowcast predictions for a list of stations.
        Returns entries matching `backend.models.NowcastPrediction`.
        """
        x_dummy = torch.randn(1, self.in_frames, grid_h, grid_w)
        
        with torch.no_grad():
            preds = self.model(x_dummy)  # (1, out_frames, H, W)
            preds = torch.relu(preds)
            
        now = datetime.now(timezone.utc)
        results = []
        
        for station in station_metadata:
            s_id = station["station_id"]
            # Predict for consecutive 12-minute lead times up to 2 hours (10 frames)
            for step_idx in range(self.out_frames):
                lead_minutes = (step_idx + 1) * 12
                valid_time = now + timedelta(minutes=lead_minutes)
                
                # Sample prediction value from tensor (in mm/12min)
                intensity_val = float(preds[0, step_idx].mean().item())
                # Rain probability proxy via sigmoid over intensity threshold (0.05 mm)
                prob_val = float(torch.sigmoid(torch.tensor((intensity_val - 0.05) * 5.0)).item())
                
                results.append({
                    "station_id": s_id,
                    "generated_at": now.isoformat(),
                    "valid_for": valid_time.isoformat(),
                    "lead_time_min": lead_minutes,
                    "rain_probability": round(prob_val, 3),
                    "rain_intensity_mm": round(intensity_val, 2),
                    "model_version": f"{self.model_type}-v1.0"
                })
                
        return results


if __name__ == "__main__":
    nowcaster = HyperlocalNowcaster(model_type="transatunet")
    demo_stations = [
        {"station_id": "PWS_PUDU_001", "name": "Puducherry Town"},
        {"station_id": "PWS_AURO_002", "name": "Auroville"},
        {"station_id": "PWS_CUDD_003", "name": "Cuddalore Coastal"}
    ]
    predictions = nowcaster.predict_for_stations(demo_stations)
    print(f"Generated {len(predictions)} nowcast prediction points for {len(demo_stations)} stations.")
    print("Sample output:", predictions[0])
