"""
Pydantic schemas for REST API serialization.
"""

from datetime import datetime, timezone
from typing import Optional, List
from pydantic import BaseModel, field_serializer


# ── Station ──────────────────────────────────────────────────────────

class StationBase(BaseModel):
    station_id: str
    name: str
    source: str
    lat: float
    lon: float
    city: Optional[str] = None
    state: str = "Tamil Nadu"


class StationOut(StationBase):
    id: int
    is_active: bool = True
    latest_reading: Optional["WeatherReadingOut"] = None

    model_config = {"from_attributes": True}


# ── Weather Reading ──────────────────────────────────────────────────

class WeatherReadingOut(BaseModel):
    id: int
    station_id: str
    source: str
    timestamp: datetime
    temp_c: Optional[float] = None
    humidity_pct: Optional[float] = None
    pressure_hpa: Optional[float] = None
    wind_speed_kmh: Optional[float] = None
    wind_dir_deg: Optional[float] = None
    rainfall_mm: Optional[float] = None
    dew_point_c: Optional[float] = None
    lat: Optional[float] = None
    lon: Optional[float] = None

    model_config = {"from_attributes": True}

    @field_serializer("timestamp")
    def serialize_timestamp(self, dt: datetime, _info) -> str:
        """Ensure timestamps are always serialized with ISO 8601 'Z' UTC indicator."""
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.isoformat().replace("+00:00", "Z")


# ── Nowcast Prediction ───────────────────────────────────────────────

class NowcastPredictionOut(BaseModel):
    id: int
    station_id: str
    generated_at: datetime
    valid_for: datetime
    rain_probability: Optional[float] = None
    rain_intensity_mm: Optional[float] = None
    model_version: str = "baseline-v0"

    model_config = {"from_attributes": True}


# ── Aggregated responses ─────────────────────────────────────────────

class DashboardOverview(BaseModel):
    total_stations: int
    active_stations: int
    total_readings: int
    latest_ingestion: Optional[datetime] = None
    avg_temp_c: Optional[float] = None
    avg_humidity_pct: Optional[float] = None
    max_rainfall_mm: Optional[float] = None

    @field_serializer("latest_ingestion")
    def serialize_latest_ingestion(self, dt: Optional[datetime], _info) -> Optional[str]:
        if dt is None:
            return None
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.isoformat().replace("+00:00", "Z")


StationOut.model_rebuild()
