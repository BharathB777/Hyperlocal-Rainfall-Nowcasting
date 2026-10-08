"""
Open-Meteo adapter — free weather API, no key required.
Provides current conditions and 24-48h hourly history for configured
Tamil Nadu / Puducherry locations.
"""

import logging
from datetime import datetime, timezone
from typing import List

import httpx

from adapters import WeatherAdapter, WeatherDataPoint
from config import get_settings

logger = logging.getLogger(__name__)

OPEN_METEO_STATIONS = [
    {"id": "OM-CHENNAI-01",   "name": "Chennai Central",       "city": "Chennai",       "lat": 13.0827, "lon": 80.2707},
    {"id": "OM-PONDY-01",     "name": "Puducherry Town",       "city": "Puducherry",    "lat": 11.9416, "lon": 79.8083},
    {"id": "OM-MADURAI-01",   "name": "Madurai Central",       "city": "Madurai",       "lat": 9.9252,  "lon": 78.1198},
    {"id": "OM-COIMBAT-01",   "name": "Coimbatore City",       "city": "Coimbatore",    "lat": 11.0168, "lon": 76.9558},
    {"id": "OM-TIRUCHI-01",   "name": "Tiruchirappalli City",  "city": "Tiruchirappalli", "lat": 10.7905, "lon": 78.7047},
    {"id": "OM-SALEM-01",     "name": "Salem City",            "city": "Salem",         "lat": 11.6643, "lon": 78.1460},
    {"id": "OM-VELLORE-01",   "name": "Vellore City",          "city": "Vellore",       "lat": 12.9165, "lon": 79.1325},
    {"id": "OM-TIRUNELV-01",  "name": "Tirunelveli City",      "city": "Tirunelveli",   "lat": 8.7139,  "lon": 77.7567},
    {"id": "OM-THOOTHU-01",   "name": "Thoothukudi Port",      "city": "Thoothukudi",   "lat": 8.7642,  "lon": 78.1348},
    {"id": "OM-CUDDALO-01",   "name": "Cuddalore Town",        "city": "Cuddalore",     "lat": 11.7480, "lon": 79.7714},
]


class OpenMeteoAdapter(WeatherAdapter):
    """
    Fetches current weather and historical hourly time-series
    from the Open-Meteo API.
    """

    def __init__(self):
        self.settings = get_settings()
        self.base_url = self.settings.OPEN_METEO_BASE_URL

    @property
    def source_name(self) -> str:
        return "open-meteo"

    def is_available(self) -> bool:
        return True

    async def fetch_readings(self) -> List[WeatherDataPoint]:
        """Fetch current conditions for all TN/Puducherry stations."""
        readings: List[WeatherDataPoint] = []

        lats = ",".join(str(s["lat"]) for s in OPEN_METEO_STATIONS)
        lons = ",".join(str(s["lon"]) for s in OPEN_METEO_STATIONS)

        params = {
            "latitude": lats,
            "longitude": lons,
            "current": ",".join([
                "temperature_2m",
                "relative_humidity_2m",
                "surface_pressure",
                "wind_speed_10m",
                "wind_direction_10m",
                "rain",
                "dew_point_2m",
            ]),
            "timezone": "Asia/Kolkata",
        }

        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                resp = await client.get(f"{self.base_url}/v1/forecast", params=params)
                resp.raise_for_status()
                data = resp.json()

            if isinstance(data, dict):
                data = [data]

            for station_cfg, result in zip(OPEN_METEO_STATIONS, data):
                current = result.get("current", {})
                if not current:
                    continue

                ts_str = current.get("time", "")
                try:
                    ts = datetime.fromisoformat(ts_str).replace(tzinfo=timezone.utc)
                except (ValueError, TypeError):
                    ts = datetime.now(timezone.utc)

                readings.append(WeatherDataPoint(
                    station_id=station_cfg["id"],
                    source="open-meteo",
                    timestamp=ts,
                    temp_c=current.get("temperature_2m"),
                    humidity_pct=current.get("relative_humidity_2m"),
                    pressure_hpa=current.get("surface_pressure"),
                    wind_speed_kmh=current.get("wind_speed_10m"),
                    wind_dir_deg=current.get("wind_direction_10m"),
                    rainfall_mm=current.get("rain"),
                    dew_point_c=current.get("dew_point_2m"),
                    lat=station_cfg["lat"],
                    lon=station_cfg["lon"],
                    station_name=station_cfg["name"],
                    city=station_cfg["city"],
                    state="Tamil Nadu" if station_cfg["city"] != "Puducherry" else "Puducherry",
                ))

            logger.info(f"[Open-Meteo] Fetched {len(readings)} live readings")

        except Exception as e:
            logger.error(f"[Open-Meteo] Live fetch error: {e}")

        return readings

    async def fetch_history(self, past_days: int = 2) -> List[WeatherDataPoint]:
        """
        Fetch the past N days of hourly weather observations for all stations
        to backfill continuous time-series curves.
        """
        historical_points: List[WeatherDataPoint] = []

        lats = ",".join(str(s["lat"]) for s in OPEN_METEO_STATIONS)
        lons = ",".join(str(s["lon"]) for s in OPEN_METEO_STATIONS)

        params = {
            "latitude": lats,
            "longitude": lons,
            "past_days": past_days,
            "forecast_days": 1,
            "hourly": ",".join([
                "temperature_2m",
                "relative_humidity_2m",
                "surface_pressure",
                "wind_speed_10m",
                "wind_direction_10m",
                "rain",
                "dew_point_2m",
            ]),
            "timezone": "Asia/Kolkata",
        }

        try:
            async with httpx.AsyncClient(timeout=40.0) as client:
                resp = await client.get(f"{self.base_url}/v1/forecast", params=params)
                resp.raise_for_status()
                data = resp.json()

            if isinstance(data, dict):
                data = [data]

            now_utc = datetime.now(timezone.utc)

            for station_cfg, result in zip(OPEN_METEO_STATIONS, data):
                hourly = result.get("hourly", {})
                times = hourly.get("time", [])
                temps = hourly.get("temperature_2m", [])
                humids = hourly.get("relative_humidity_2m", [])
                pressures = hourly.get("surface_pressure", [])
                winds = hourly.get("wind_speed_10m", [])
                dirs = hourly.get("wind_direction_10m", [])
                rains = hourly.get("rain", [])
                dews = hourly.get("dew_point_2m", [])

                for idx, t_str in enumerate(times):
                    try:
                        ts = datetime.fromisoformat(t_str).replace(tzinfo=timezone.utc)
                    except Exception:
                        continue

                    # Only ingest points up to current time (do not ingest future forecasts as past readings)
                    if ts > now_utc:
                        continue

                    historical_points.append(WeatherDataPoint(
                        station_id=station_cfg["id"],
                        source="open-meteo",
                        timestamp=ts,
                        temp_c=temps[idx] if idx < len(temps) else None,
                        humidity_pct=humids[idx] if idx < len(humids) else None,
                        pressure_hpa=pressures[idx] if idx < len(pressures) else None,
                        wind_speed_kmh=winds[idx] if idx < len(winds) else None,
                        wind_dir_deg=dirs[idx] if idx < len(dirs) else None,
                        rainfall_mm=rains[idx] if idx < len(rains) else None,
                        dew_point_c=dews[idx] if idx < len(dews) else None,
                        lat=station_cfg["lat"],
                        lon=station_cfg["lon"],
                        station_name=station_cfg["name"],
                        city=station_cfg["city"],
                        state="Tamil Nadu" if station_cfg["city"] != "Puducherry" else "Puducherry",
                    ))

            logger.info(f"[Open-Meteo] Fetched {len(historical_points)} historical hourly points for backfill")

        except Exception as e:
            logger.error(f"[Open-Meteo] Historical backfill error: {e}")

        return historical_points
