"""constants.py — Shared thresholds and flag names for the forensic accounting ecosystem.

Zero external dependencies. All values are plain Python primitives.
Numeric thresholds can be overridden via environment variables (useful in test/staging).
"""

from __future__ import annotations

import os

# Beneish M-Score detection thresholds
BENEISH_THRESHOLD: float = float(os.getenv("BENEISH_THRESHOLD", "-1.78"))
# Critical risk tier: manipulator probability is very high above this level
BENEISH_CRITICAL_THRESHOLD: float = float(os.getenv("BENEISH_CRITICAL_THRESHOLD", "-1.0"))

# High false-positive risk WICS sector codes (biotech/pharma G3510, medical devices G3520)
HIGH_FP_SECTORS: frozenset[str] = frozenset(
    s for s in os.getenv("HIGH_FP_SECTORS", "G3510,G3520").split(",") if s
)

# Model routing — never use Opus; import from here instead of hardcoding in each repo
HAIKU_MODEL: str = os.getenv("ANTHROPIC_HAIKU_MODEL", "claude-haiku-4-5-20251001")
SONNET_MODEL: str = os.getenv("ANTHROPIC_SONNET_MODEL", "claude-sonnet-4-6")

# CB/BW manipulation signal flag names
FLAG_REPRICING_BELOW_MARKET = "repricing_below_market"
FLAG_EXERCISE_AT_PEAK = "exercise_at_peak"
FLAG_VOLUME_SURGE = "volume_surge"
FLAG_HOLDINGS_DECREASE = "holdings_decrease"

# CB/BW scoring thresholds
REPRICING_DISCOUNT_RATIO: float = float(os.getenv("REPRICING_DISCOUNT_RATIO", "0.95"))
EXERCISE_PEAK_WINDOW_CALENDAR_DAYS = 5  # calendar days, intentionally NOT trading days — see Fix 1B
VOLUME_SURGE_RATIO: float = float(os.getenv("VOLUME_SURGE_RATIO", "3.0"))
HOLDINGS_DECREASE_RATIO: float = float(os.getenv("HOLDINGS_DECREASE_RATIO", "0.95"))
PRICE_WINDOW_TRADING_DAYS: int = int(os.getenv("PRICE_WINDOW_TRADING_DAYS", "60"))  # trading days (not calendar days) — see KI-043
VALID_OHLCV_BACKENDS = ("pykrx", "fdr", "yfinance")

# Timing anomaly thresholds
TIMING_PRICE_CHANGE_PCT: float = float(os.getenv("TIMING_PRICE_CHANGE_PCT", "5.0"))
TIMING_VOLUME_RATIO: float = float(os.getenv("TIMING_VOLUME_RATIO", "2.0"))
TIMING_BORDERLINE_PRICE_PCT: float = float(os.getenv("TIMING_BORDERLINE_PRICE_PCT", "3.0"))
# DART listing API returns YYYYMMDD only (no time); 18:00 KST assumed for gap_hours.
# Market close: 15:30 KST (15.5 decimal hours). Gap = 18.0 - 15.5 = 2.5 hours.
TIMING_GAP_HOURS_ASSUMED = 2.5
# Prior-day filings: ~18:00 KST filing → 09:00 open next day → 15.0 h gap.
TIMING_GAP_HOURS_PRIOR_DAY = 15.0

# Officer network — calibrated at 2 (session 33: 27 events, high precision)
OFFICER_FLAG_THRESHOLD = 2

__all__ = [
    "BENEISH_THRESHOLD",
    "BENEISH_CRITICAL_THRESHOLD",
    "HIGH_FP_SECTORS",
    "HAIKU_MODEL",
    "SONNET_MODEL",
    "FLAG_REPRICING_BELOW_MARKET",
    "FLAG_EXERCISE_AT_PEAK",
    "FLAG_VOLUME_SURGE",
    "FLAG_HOLDINGS_DECREASE",
    "REPRICING_DISCOUNT_RATIO",
    "EXERCISE_PEAK_WINDOW_CALENDAR_DAYS",
    "VOLUME_SURGE_RATIO",
    "HOLDINGS_DECREASE_RATIO",
    "PRICE_WINDOW_TRADING_DAYS",
    "VALID_OHLCV_BACKENDS",
    "TIMING_PRICE_CHANGE_PCT",
    "TIMING_VOLUME_RATIO",
    "TIMING_BORDERLINE_PRICE_PCT",
    "TIMING_GAP_HOURS_ASSUMED",
    "TIMING_GAP_HOURS_PRIOR_DAY",
    "OFFICER_FLAG_THRESHOLD",
]
