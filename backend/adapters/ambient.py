"""
PWS (Personal Weather Station) Adapter — Weather Underground & Ambient Network.

Connects to real live PWS stations in Puducherry and Auroville with high-precision
decimal temperature conversions.
"""

import logging
from datetime import datetime, timezone
from typing import List

import httpx

from adapters import WeatherAdapter, WeatherDataPoint
from config import get_settings

logger = logging.getLogger(__name__)

# ── Real PWS Stations around Puducherry & Auroville ───────────────────
REAL_PWS_STATIONS = [
    {
        "id": "IAUROV10",
        "name": "Sarvamangalam PWS",
        "city": "Auroville (Irumbai)",
        "lat": 11.98282,
        "lon": 79.80799,
        "state": "Puducherry / TN",
    },
    {
        "id": "IAUROV11",
        "name": "Auro Orchard PWS",
        "city": "Auroville (Orchard)",
        "lat": 11.98770,
        "lon": 79.79365,
        "state": "Puducherry / TN",
    },
    {
        "id": "IPONDI9",
        "name": "Heritage Town PWS",
        "city": "Puducherry (White Town)",
        "lat": 11.93600,
        "lon": 79.83300,
        "state": "Puducherry",
    },
    {
        "id": "IPONDI13",
        "name": "Marie Oulgaret PWS",
        "city": "Puducherry (Oulgaret)",
        "lat": 11.92868,
        "lon": 79.78241,
        "state": "Puducherry",
    },
    {
        "id": "IAUROV6",
        "name": "Bommayapalayam PWS",
        "city": "Auroville (Coastal)",
        "lat": 11.99030,
        "lon": 79.84118,
        "state": "Puducherry / TN",
    },
    {
        "id": "IPONDI10",
        "name": "Pondicherry South PWS",
        "city": "Puducherry (South)",
        "lat": 11.86840,
        "lon": 79.79238,
        "state": "Puducherry",
    },
]

PWS_API_KEY = "e1f10a1e78da46f5b10a1e78da96f525"
BASE_URL = "https://api.weather.com/v2/pws/observations"


class AmbientWeatherAdapter(WeatherAdapter):
    """
    Fetches real live observations with exact decimal precision from PWS network.
    """

    def __init__(self):
        self.settings = get_settings()

    @property
    def source_name(self) -> str:
        return "ambient"

    def is_available(self) -> bool:
        return True

    async def fetch_readings(self) -> List[WeatherDataPoint]:
        """Fetch current live reading for all Puducherry / Auroville PWS stations."""
        readings: List[WeatherDataPoint] = []

        async with httpx.AsyncClient(timeout=15.0) as client:
            for s in REAL_PWS_STATIONS:
                # Use imperial units for high sensor resolution, then convert to exact Celsius tenths
                url = f"{BASE_URL}/current"
                params = {
                    "stationId": s["id"],
                    "format": "json",
                    "units": "e",
                    "apiKey": PWS_API_KEY,
                }
                try:
                    resp = await client.get(url, params=params)
                    if resp.status_code != 200:
                        continue

                    data = resp.json()
                    obs_list = data.get("observations", [])
                    if not obs_list:
                        continue

                    obs = obs_list[0]
                    imp = obs.get("imperial", {})

                    # Parse observation time
                    ts_str = obs.get("obsTimeUtc")
                    try:
                        ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
                    except Exception:
                        ts = datetime.now(timezone.utc)

                    temp_f = imp.get("temp")
                    temp_c = round((temp_f - 32) * 5 / 9, 1) if temp_f is not None else None

                    dew_f = imp.get("dewpt")
                    dew_c = round((dew_f - 32) * 5 / 9, 1) if dew_f is not None else None

                    wind_mph = imp.get("windSpeed")
                    wind_kmh = round(wind_mph * 1.60934, 1) if wind_mph is not None else None

                    pressure_in = imp.get("pressure")
                    pressure_hpa = round(pressure_in * 33.8639, 1) if pressure_in is not None else None

                    rain_in = imp.get("precipTotal", 0.0)
                    rain_mm = round(rain_in * 25.4, 2) if rain_in is not None else 0.0

                    readings.append(WeatherDataPoint(
                        station_id=s["id"],
                        source="ambient",
                        timestamp=ts,
                        temp_c=temp_c,
                        humidity_pct=obs.get("humidity"),
                        pressure_hpa=pressure_hpa,
                        wind_speed_kmh=wind_kmh,
                        wind_dir_deg=obs.get("winddir"),
                        rainfall_mm=rain_mm,
                        dew_point_c=dew_c,
                        lat=obs.get("lat") or s["lat"],
                        lon=obs.get("lon") or s["lon"],
                        station_name=s["name"],
                        city=s["city"],
                        state=s["state"],
                    ))
                except Exception as e:
                    logger.error(f"[PWS] Error fetching {s['id']}: {e}")

        logger.info(f"[PWS/Ambient] Fetched {len(readings)} live real PWS readings")
        return readings

    async def fetch_history(self, hours: int = 48) -> List[WeatherDataPoint]:
        """
        Fetch real historical hourly observations from Weather Underground 7-day endpoint.
        """
        history_points: List[WeatherDataPoint] = []

        async with httpx.AsyncClient(timeout=20.0) as client:
            for s in REAL_PWS_STATIONS:
                url = f"{BASE_URL}/hourly/7day"
                params = {
                    "stationId": s["id"],
                    "format": "json",
                    "units": "e",
                    "apiKey": PWS_API_KEY,
                }
                try:
                    resp = await client.get(url, params=params)
                    if resp.status_code != 200:
                        continue

                    data = resp.json()
                    obs_list = data.get("observations", [])

                    recent_obs = obs_list[-hours:] if len(obs_list) > hours else obs_list

                    for obs in recent_obs:
                        imp = obs.get("imperial", {})
                        ts_str = obs.get("obsTimeUtc")
                        try:
                            ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
                        except Exception:
                            continue

                        temp_f = imp.get("tempAvg") if imp.get("tempAvg") is not None else imp.get("tempHigh")
                        temp_c = round((temp_f - 32) * 5 / 9, 1) if temp_f is not None else None

                        dew_f = imp.get("dewptAvg") if imp.get("dewptAvg") is not None else imp.get("dewptHigh")
                        dew_c = round((dew_f - 32) * 5 / 9, 1) if dew_f is not None else None

                        wind_mph = imp.get("windspeedAvg") if imp.get("windspeedAvg") is not None else imp.get("windspeedHigh")
                        wind_kmh = round(wind_mph * 1.60934, 1) if wind_mph is not None else None

                        pressure_in = imp.get("pressureMax") if imp.get("pressureMax") is not None else imp.get("pressureMin")
                        pressure_hpa = round(pressure_in * 33.8639, 1) if pressure_in is not None else None

                        rain_in = imp.get("precipTotal", 0.0)
                        rain_mm = round(rain_in * 25.4, 2) if rain_in is not None else 0.0

                        history_points.append(WeatherDataPoint(
                            station_id=s["id"],
                            source="ambient",
                            timestamp=ts,
                            temp_c=temp_c,
                            humidity_pct=obs.get("humidityAvg") or obs.get("humidityHigh"),
                            pressure_hpa=pressure_hpa,
                            wind_speed_kmh=wind_kmh,
                            wind_dir_deg=obs.get("winddirAvg"),
                            rainfall_mm=rain_mm,
                            dew_point_c=dew_c,
                            lat=obs.get("lat") or s["lat"],
                            lon=obs.get("lon") or s["lon"],
                            station_name=s["name"],
                            city=s["city"],
                            state=s["state"],
                        ))

                except Exception as e:
                    logger.error(f"[PWS] Error backfilling history for {s['id']}: {e}")

        logger.info(f"[PWS/Ambient] Fetched {len(history_points)} real historical points for Puducherry/Auroville PWS")
        return history_points
