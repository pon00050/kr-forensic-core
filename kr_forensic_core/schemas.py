"""schemas.py — Parquet table registry and column specifications.

Single source of truth for logical table names → filenames and expected columns.
Zero external dependencies.
"""

from __future__ import annotations

# Logical table names → parquet filenames
PARQUET_TABLES: dict[str, str] = {
    "company_financials": "company_financials.parquet",
    "beneish_scores": "beneish_scores.parquet",
    "cb_bw_events": "cb_bw_events.parquet",
    "price_volume": "price_volume.parquet",
    "corp_ticker_map": "corp_ticker_map.parquet",
    "officer_holdings": "officer_holdings.parquet",
    "disclosures": "disclosures.parquet",
    "major_holders": "major_holders.parquet",
    "bondholder_register": "bondholder_register.parquet",
    "revenue_schedule": "revenue_schedule.parquet",
    "bond_isin_map": "bond_isin_map.parquet",
}

# Minimum expected columns per table (used for schema validation at boundaries)
BENEISH_SCORES_COLUMNS = {"corp_code", "year", "m_score"}
PRICE_VOLUME_COLUMNS = {"ticker", "date", "close", "volume"}
CB_BW_EVENTS_COLUMNS = {"corp_code", "issue_date", "bond_type"}
CORP_TICKER_MAP_COLUMNS = {"corp_code", "ticker"}
OFFICER_HOLDINGS_COLUMNS = {"corp_code", "date", "change_shares"}
DISCLOSURES_COLUMNS = {"corp_code", "trading_date", "title"}

__all__ = [
    "PARQUET_TABLES",
    "BENEISH_SCORES_COLUMNS",
    "PRICE_VOLUME_COLUMNS",
    "CB_BW_EVENTS_COLUMNS",
    "CORP_TICKER_MAP_COLUMNS",
    "OFFICER_HOLDINGS_COLUMNS",
    "DISCLOSURES_COLUMNS",
]
