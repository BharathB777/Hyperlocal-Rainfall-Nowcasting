"""
Database engine, session factory, and base model.
Supports SQLite (local dev) and PostgreSQL (production) via DATABASE_URL.
"""

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from config import get_settings

settings = get_settings()

# ── Engine ───────────────────────────────────────────────────────────
# For SQLite we need check_same_thread=False; PostgreSQL ignores it.
connect_args = {}
if settings.DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,
    connect_args=connect_args,
)

# ── Session factory ──────────────────────────────────────────────────
async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# ── Base class for ORM models ────────────────────────────────────────
class Base(DeclarativeBase):
    pass


# ── Dependency for FastAPI route injection ───────────────────────────
async def get_db() -> AsyncSession:
    """Yields a database session; auto-closes on exit."""
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


# ── Table creation utility ───────────────────────────────────────────
async def create_tables():
    """Create all tables defined by ORM models. Safe to call repeatedly."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
