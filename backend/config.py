"""
Application configuration loaded from environment variables.
"""

from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Central configuration – reads from .env file at project root."""

    # ── Ambient Weather API ──────────────────────────────────────────
    AMBIENT_API_KEY: str = ""
    AMBIENT_APP_KEY: str = ""

    # ── Open-Meteo (free, no key required) ───────────────────────────
    OPEN_METEO_BASE_URL: str = "https://api.open-meteo.com"

    # ── IMD AWS API (pending approval) ───────────────────────────────
    IMD_API_TOKEN: str = ""

    # ── Database ─────────────────────────────────────────────────────
    DATABASE_URL: str = "sqlite+aiosqlite:///./weather.db"

    # ── Auth (Phase 2) ───────────────────────────────────────────────
    NEXTAUTH_SECRET: str = ""
    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_CLIENT_SECRET: str = ""
    FACEBOOK_CLIENT_ID: str = ""
    FACEBOOK_CLIENT_SECRET: str = ""

    # ── CORS ─────────────────────────────────────────────────────────
    FRONTEND_URL: str = "http://localhost:3000"

    # ── Ingestion Interval (60 seconds for live PWS syncing) ─────────
    INGESTION_INTERVAL_SECONDS: int = 60
    INGESTION_INTERVAL_MINUTES: int = 1

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": True,
        "extra": "ignore",
    }


@lru_cache()
def get_settings() -> Settings:
    return Settings()
