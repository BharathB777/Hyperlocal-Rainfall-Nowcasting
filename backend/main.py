"""
Hyperlocal Rainfall Nowcasting — FastAPI Backend
Main application entry point.

Configures:
  - CORS for frontend communication
  - Root landing `/` with service metadata and documentation links
  - API routes (weather data, stations, nowcast)
  - 24-48h historical backfill on startup
  - Background ingestion scheduler (APScheduler)
"""

import asyncio
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from config import get_settings
from database import create_tables
from ingestion import run_ingestion, backfill_history
from routers.weather import router as weather_router

# ── Logging setup ────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s │ %(levelname)-7s │ %(name)-20s │ %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("nowcast")

settings = get_settings()
scheduler = AsyncIOScheduler()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Startup / shutdown lifecycle.
    """
    logger.info("🌧️  Hyperlocal Rainfall Nowcasting — Backend starting...")

    # 1. Create all DB tables
    await create_tables()
    logger.info("✅ Database tables ready")

    # 2. Run historical 24-48h backfill so graphs have full continuous curves
    logger.info("⏳ Backfilling 24-48h historical time-series telemetry...")
    await backfill_history()

    # 3. Ingest latest live snapshot
    logger.info("🔄 Running initial live data ingestion...")
    await run_ingestion()

    # 4. Schedule high-frequency periodic ingestion (every 60s for PWS)
    scheduler.add_job(
        run_ingestion,
        trigger=IntervalTrigger(seconds=settings.INGESTION_INTERVAL_SECONDS),
        id="weather_ingestion",
        name="Weather Data Ingestion",
        replace_existing=True,
    )
    scheduler.start()
    logger.info(f"⏰ High-frequency ingestion scheduled every {settings.INGESTION_INTERVAL_SECONDS} seconds")

    yield

    scheduler.shutdown(wait=False)
    logger.info("🛑 Scheduler stopped. Backend shutting down.")


# ── FastAPI App ──────────────────────────────────────────────────────
app = FastAPI(
    title="Hyperlocal Rainfall Nowcasting API",
    description=(
        "Multi-source weather data fusion platform for Tamil Nadu & Puducherry. "
        "Fuses IMD AWS, Personal Weather Stations (PWS), and ECMWF NWP forecasts."
    ),
    version="0.1.0",
    lifespan=lifespan,
)

# ── CORS ─────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Root Landing Endpoint ────────────────────────────────────────────
@app.get("/", response_class=HTMLResponse)
async def root():
    """
    Root landing page showing backend service information and links to Swagger UI and API endpoints.
    """
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>NowCast TN — Backend API</title>
        <style>
            body {
                background: #0A1628;
                color: #E8F1F8;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                margin: 0;
                padding: 40px 20px;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                box-sizing: border-box;
            }
            .card {
                background: rgba(16, 32, 56, 0.85);
                border: 1px solid rgba(28, 114, 147, 0.3);
                border-radius: 16px;
                padding: 32px;
                max-width: 600px;
                width: 100%;
                box-shadow: 0 8px 32px rgba(0,0,0,0.4);
            }
            h1 { color: #00D4FF; margin-top: 0; font-size: 24px; }
            p { color: #8BA4B8; line-height: 1.6; font-size: 14px; }
            .badge {
                display: inline-block;
                background: rgba(6, 214, 160, 0.15);
                color: #06D6A0;
                padding: 4px 10px;
                border-radius: 8px;
                font-weight: bold;
                font-size: 12px;
                margin-bottom: 16px;
            }
            .links { margin-top: 24px; display: flex; flex-direction: column; gap: 10px; }
            a {
                display: block;
                background: #065A82;
                color: white;
                text-decoration: none;
                padding: 12px 16px;
                border-radius: 10px;
                font-weight: 500;
                font-size: 14px;
                transition: 0.2s;
            }
            a:hover { background: #1C7293; transform: translateY(-2px); }
            .sublink { background: rgba(255,255,255,0.05); color: #8BA4B8; border: 1px solid rgba(28, 114, 147, 0.2); }
            .sublink:hover { color: #E8F1F8; background: rgba(255,255,255,0.1); }
        </style>
    </head>
    <body>
        <div class="card">
            <span class="badge">● SYSTEM ONLINE (PORT 8000)</span>
            <h1>Hyperlocal Rainfall Nowcasting API</h1>
            <p>
                Multi-source weather data fusion backend for Tamil Nadu & Puducherry.
                Telemetry actively streaming from IMD AWS, Community Personal Weather Stations (PWS), and ECMWF NWP models.
            </p>
            <div class="links">
                <a href="/docs">📖 Open Interactive Swagger API Docs (/docs)</a>
                <a href="/api/overview" class="sublink">📊 GET /api/overview — System Telemetry Summary</a>
                <a href="/api/stations" class="sublink">📡 GET /api/stations — Active Weather Stations</a>
                <a href="http://localhost:3000" class="sublink" target="_blank">🌐 Open Next.js Frontend Dashboard (localhost:3000)</a>
            </div>
        </div>
    </body>
    </html>
    """


@app.get("/health")
async def health():
    return {"status": "ok", "service": "nowcast-backend"}


# ── Mount Routers ────────────────────────────────────────────────────
app.include_router(weather_router)
