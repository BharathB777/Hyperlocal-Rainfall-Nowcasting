"""
Abstract base class for all weather data adapters.
Every data source (Ambient, Open-Meteo, IMD) implements this interface,
ensuring the ingestion pipeline is completely source-agnostic.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class WeatherDataPoint:
    """
    Source-agnostic weather observation.
    All adapters produce a list of these; the ingestion service writes them to DB.
    """
    station_id: str
    source: str                     # "ambient" | "imd" | "open-meteo"
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

    # Station metadata (used to upsert the stations table)
    station_name: Optional[str] = None
    city: Optional[str] = None
    state: str = "Tamil Nadu"
    elevation_m: Optional[float] = None


class WeatherAdapter(ABC):
    """
    Abstract adapter interface.

    Implementations:
        - AmbientWeatherAdapter  (ambient.py)
        - OpenMeteoAdapter       (openmeteo.py)
        - IMDAdapter             (imd.py) — stubbed until API access approved
    """

    @property
    @abstractmethod
    def source_name(self) -> str:
        """Return the source identifier, e.g. 'ambient', 'open-meteo', 'imd'."""
        ...

    @abstractmethod
    async def fetch_readings(self) -> List[WeatherDataPoint]:
        """
        Fetch the latest weather observations from this source.
        Returns a list of WeatherDataPoint instances.
        Must handle API failures gracefully (log + return empty list).
        """
        ...

    @abstractmethod
    def is_available(self) -> bool:
        """
        Check if this adapter is configured and ready to use.
        E.g., returns False if required API keys are missing.
        """
        ...
