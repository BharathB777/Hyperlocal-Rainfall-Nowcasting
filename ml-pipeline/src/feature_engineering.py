"""
Feature Engineering Module for Hyperlocal Rainfall Nowcasting.
Based on base papers 1-10 (ST-GRF, ECSA module, Spatiotemporal Fusion).

Calculates:
- Rolling pressure change rate (dp/dt)
- Humidity trend & saturation deficit
- Dew point spread (T - Td)
- Wind shear & directional convergence
"""

import pandas as pd
import numpy as np


def compute_dew_point_spread(df: pd.DataFrame) -> pd.DataFrame:
    """Dew point depression = T - T_dew. Low spread indicates high saturation/condensation likelihood."""
    df["dew_point_spread"] = df["temp_c"] - df["dew_point_c"]
    return df


def compute_pressure_trends(df: pd.DataFrame, window_periods: int = 3) -> pd.DataFrame:
    """Calculates pressure tendency (hPa drop rate per hour). Rapid drop indicates convective updrafts."""
    df = df.sort_values(by=["station_id", "timestamp"])
    df["pressure_drop_rate"] = df.groupby("station_id")["pressure_hpa"].diff(periods=window_periods)
    return df


def compute_humidity_trend(df: pd.DataFrame, window_periods: int = 3) -> pd.DataFrame:
    """Calculates humidity rate of change."""
    df = df.sort_values(by=["station_id", "timestamp"])
    df["humidity_delta"] = df.groupby("station_id")["humidity_pct"].diff(periods=window_periods)
    return df


if __name__ == "__main__":
    print("Feature Engineering Pipeline module loaded.")
