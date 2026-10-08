"""
IMD AWS (Automatic Weather Station) adapter — STUBBED.

This adapter implements the WeatherAdapter interface but is not functional yet.
IMD API access requires a formal approval process. Once access is granted,
implement the fetch_readings() method to pull station data from the IMD API.

The adapter pattern means this is the ONLY file that needs to change when
IMD access is approved — no downstream code modifications required.
"""

import logging
from typing import List

from adapters import WeatherAdapter, WeatherDataPoint

logger = logging.getLogger(__name__)


class IMDAdapter(WeatherAdapter):
    """
    Indian Meteorological Department Automatic Weather Station adapter.

    STATUS: STUBBED — blocked on API access approval.
    TODO: Implement once IMD API token is received.
    """

    def __init__(self, api_token: str = ""):
        self.api_token = api_token

    @property
    def source_name(self) -> str:
        return "imd"

    def is_available(self) -> bool:
        """Returns False until IMD API access is configured."""
        return bool(self.api_token)

    async def fetch_readings(self) -> List[WeatherDataPoint]:
        """
        TODO: Implement when IMD API access is approved.

        Expected implementation:
        1. Call the IMD AWS REST API with the auth token
        2. Parse the response JSON (station observations)
        3. Map fields to WeatherDataPoint instances
        4. Return list of readings

        IMD AWS stations typically report:
        - Temperature, humidity, pressure
        - Wind speed/direction
        - Rainfall (accumulated)
        - Station coordinates and metadata
        """
        if not self.is_available():
            logger.debug("[IMD] Skipped — API token not configured (pending approval)")
            return []

        # ──────────────────────────────────────────────────────────────
        # PLACEHOLDER: Replace this block with actual API call
        # ──────────────────────────────────────────────────────────────
        logger.warning("[IMD] Adapter not yet implemented — awaiting API access")
        return []
