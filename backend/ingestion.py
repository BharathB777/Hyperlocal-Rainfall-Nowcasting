"""
Scheduled ingestion & history backfill service.
Runs every N minutes, fetches from all active adapters,
deduplicates readings, and bulk-inserts into the database.
"""

import logging
from datetime import datetime, timezone

from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from adapters import WeatherDataPoint
from adapters.openmeteo import OpenMeteoAdapter
from adapters.ambient import AmbientWeatherAdapter
from adapters.imd import IMDAdapter
from config import get_settings
from database import async_session
from models import WeatherReading, Station

logger = logging.getLogger(__name__)

settings = get_settings()

om_adapter = OpenMeteoAdapter()
amb_adapter = AmbientWeatherAdapter()
imd_adapter = IMDAdapter(api_token=settings.IMD_API_TOKEN)

ADAPTERS = [om_adapter, amb_adapter, imd_adapter]


async def backfill_history():
    """
    Backfills 24-48 hours of historical readings for all stations on startup.
    Ensures the trend charts immediately have rich, continuous time-series curves.
    """
    logger.info("─── Starting 24-48h historical backfill ───")
    total_backfilled = 0

    async with async_session() as session:
        # 1. Backfill Open-Meteo hourly history
        try:
            om_history = await om_adapter.fetch_history(past_days=2)
            for dp in om_history:
                await _upsert_station(session, dp)
                if not await _reading_exists(session, dp):
                    session.add(_to_model(dp))
                    total_backfilled += 1
        except Exception as e:
            logger.error(f"Error backfilling Open-Meteo: {e}")

        # 2. Backfill Ambient / Community PWS history
        try:
            amb_history = await amb_adapter.fetch_history(hours=48)
            for dp in amb_history:
                await _upsert_station(session, dp)
                if not await _reading_exists(session, dp):
                    session.add(_to_model(dp))
                    total_backfilled += 1
        except Exception as e:
            logger.error(f"Error backfilling Ambient PWS: {e}")

        await session.commit()

    logger.info(f"✅ Historical backfill complete: {total_backfilled} time-series points inserted.")


async def run_ingestion():
    """
    Periodic ingestion loop — runs every 10 minutes.
    """
    logger.info("─── Ingestion cycle started ───")
    total_new = 0

    async with async_session() as session:
        for adapter in ADAPTERS:
            if not adapter.is_available():
                continue

            try:
                data_points = await adapter.fetch_readings()
                for dp in data_points:
                    await _upsert_station(session, dp)
                    if not await _reading_exists(session, dp):
                        session.add(_to_model(dp))
                        total_new += 1
            except Exception as e:
                logger.error(f"[{adapter.source_name}] Ingestion error: {e}")

        await session.commit()

    logger.info(f"─── Ingestion complete: {total_new} new readings inserted ───")


async def _reading_exists(session: AsyncSession, dp: WeatherDataPoint) -> bool:
    res = await session.execute(
        select(WeatherReading.id).where(
            and_(
                WeatherReading.station_id == dp.station_id,
                WeatherReading.timestamp == dp.timestamp,
            )
        )
    )
    return res.scalar_one_or_none() is not None


def _to_model(dp: WeatherDataPoint) -> WeatherReading:
    return WeatherReading(
        station_id=dp.station_id,
        source=dp.source,
        timestamp=dp.timestamp,
        temp_c=dp.temp_c,
        humidity_pct=dp.humidity_pct,
        pressure_hpa=dp.pressure_hpa,
        wind_speed_kmh=dp.wind_speed_kmh,
        wind_dir_deg=dp.wind_dir_deg,
        rainfall_mm=dp.rainfall_mm,
        dew_point_c=dp.dew_point_c,
        lat=dp.lat,
        lon=dp.lon,
    )


async def _upsert_station(session: AsyncSession, dp: WeatherDataPoint):
    result = await session.execute(
        select(Station).where(Station.station_id == dp.station_id)
    )
    station = result.scalar_one_or_none()

    if station is None:
        station = Station(
            station_id=dp.station_id,
            name=dp.station_name or dp.station_id,
            source=dp.source,
            lat=dp.lat or 0.0,
            lon=dp.lon or 0.0,
            elevation_m=dp.elevation_m,
            city=dp.city,
            state=dp.state,
            is_active=1,
        )
        session.add(station)
