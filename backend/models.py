"""
SQLAlchemy ORM models for the weather platform.
Schema matches the project brief's data definitions.
"""

from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Float, DateTime, UniqueConstraint, Index, Text
)
from database import Base


class Station(Base):
    """
    Metadata for a weather station — either a physical Ambient PWS,
    an IMD AWS station, or an Open-Meteo virtual point.
    """
    __tablename__ = "stations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    station_id = Column(String(64), unique=True, nullable=False, index=True)
    name = Column(String(256), nullable=False)
    source = Column(String(32), nullable=False)  # "ambient" | "imd" | "open-meteo"
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    elevation_m = Column(Float, nullable=True)
    city = Column(String(128), nullable=True)
    state = Column(String(64), default="Tamil Nadu")
    is_active = Column(Integer, default=1)  # SQLite-safe boolean
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Station {self.station_id} ({self.source})>"


class WeatherReading(Base):
    """
    Time-series weather observation — one row per station per timestamp.
    This is the core table; expect millions of rows over time.
    """
    __tablename__ = "weather_readings"
    __table_args__ = (
        UniqueConstraint("station_id", "timestamp", name="uq_station_timestamp"),
        Index("ix_readings_station_time", "station_id", "timestamp"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    station_id = Column(String(64), nullable=False, index=True)
    source = Column(String(32), nullable=False)
    timestamp = Column(DateTime, nullable=False, index=True)
    temp_c = Column(Float, nullable=True)
    humidity_pct = Column(Float, nullable=True)
    pressure_hpa = Column(Float, nullable=True)
    wind_speed_kmh = Column(Float, nullable=True)
    wind_dir_deg = Column(Float, nullable=True)
    rainfall_mm = Column(Float, nullable=True)
    dew_point_c = Column(Float, nullable=True)
    lat = Column(Float, nullable=True)
    lon = Column(Float, nullable=True)

    def __repr__(self):
        return f"<Reading {self.station_id} @ {self.timestamp}>"


class NowcastPrediction(Base):
    """
    AI nowcast predictions — generated every 10-15 minutes per station.
    Phase 2: populated by the ML inference service.
    """
    __tablename__ = "nowcast_predictions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    station_id = Column(String(64), nullable=False, index=True)
    generated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    valid_for = Column(DateTime, nullable=False)
    rain_probability = Column(Float, nullable=True)
    rain_intensity_mm = Column(Float, nullable=True)
    model_version = Column(String(32), default="baseline-v0")

    def __repr__(self):
        return f"<Nowcast {self.station_id} valid_for={self.valid_for}>"


class BlogPost(Base):
    """Blog posts — manual or auto-fetched from social media. Phase 2."""
    __tablename__ = "blog_posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(512), nullable=False)
    slug = Column(String(512), unique=True, nullable=False)
    content = Column(Text, nullable=False)
    source = Column(String(32), default="manual")  # "manual" | "facebook" | "x"
    published_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<BlogPost {self.slug}>"
