"""Guard tests for threshold values.

These tests exist to prevent silent threshold drift — changing a value
requires updating this test, making the change deliberate and visible.
"""

import pytest
from kr_forensic_core.constants import (
    BENEISH_THRESHOLD,
    FLAG_REPRICING_BELOW_MARKET,
    FLAG_EXERCISE_AT_PEAK,
    FLAG_VOLUME_SURGE,
    FLAG_HOLDINGS_DECREASE,
    REPRICING_DISCOUNT_RATIO,
    EXERCISE_PEAK_WINDOW_CALENDAR_DAYS,
    VOLUME_SURGE_RATIO,
    HOLDINGS_DECREASE_RATIO,
    PRICE_WINDOW_TRADING_DAYS,
    TIMING_PRICE_CHANGE_PCT,
    TIMING_VOLUME_RATIO,
    TIMING_BORDERLINE_PRICE_PCT,
    TIMING_GAP_HOURS_ASSUMED,
    TIMING_GAP_HOURS_PRIOR_DAY,
    OFFICER_FLAG_THRESHOLD,
)
from kr_forensic_core.schemas import PARQUET_TABLES
from kr_forensic_core.paths import data_dir
import os


def test_beneish_threshold():
    assert BENEISH_THRESHOLD == -1.78


def test_flag_names_are_strings():
    for flag in (FLAG_REPRICING_BELOW_MARKET, FLAG_EXERCISE_AT_PEAK, FLAG_VOLUME_SURGE, FLAG_HOLDINGS_DECREASE):
        assert isinstance(flag, str)
        assert len(flag) > 0


def test_cb_bw_thresholds():
    assert REPRICING_DISCOUNT_RATIO == 0.95
    assert EXERCISE_PEAK_WINDOW_CALENDAR_DAYS == 5
    assert VOLUME_SURGE_RATIO == 3.0
    assert HOLDINGS_DECREASE_RATIO == 0.95
    assert PRICE_WINDOW_TRADING_DAYS == 60


def test_timing_thresholds():
    assert TIMING_PRICE_CHANGE_PCT == 5.0
    assert TIMING_VOLUME_RATIO == 2.0
    assert TIMING_BORDERLINE_PRICE_PCT == 3.0
    assert TIMING_GAP_HOURS_ASSUMED == 2.5
    assert TIMING_GAP_HOURS_PRIOR_DAY == 15.0


def test_officer_threshold():
    assert OFFICER_FLAG_THRESHOLD == 2


def test_parquet_tables_registry():
    assert "beneish_scores" in PARQUET_TABLES
    assert "price_volume" in PARQUET_TABLES
    assert "cb_bw_events" in PARQUET_TABLES
    assert "corp_ticker_map" in PARQUET_TABLES
    # All values end in .parquet
    for key, val in PARQUET_TABLES.items():
        assert val.endswith(".parquet"), f"{key} → {val} should end in .parquet"


def test_data_dir_from_env(tmp_path, monkeypatch):
    monkeypatch.setenv("KRFF_DATA_DIR", str(tmp_path))
    result = data_dir()
    assert result == tmp_path


def test_data_dir_from_repo_root(tmp_path):
    result = data_dir(repo_root=tmp_path)
    assert result == tmp_path / "01_Data" / "processed"


def test_data_dir_no_args_raises():
    env_backup = os.environ.pop("KRFF_DATA_DIR", None)
    try:
        with pytest.raises(ValueError):
            data_dir()
    finally:
        if env_backup is not None:
            os.environ["KRFF_DATA_DIR"] = env_backup


def test_top_level_imports():
    """Verify __init__.py re-exports work."""
    import kr_forensic_core
    assert hasattr(kr_forensic_core, "BENEISH_THRESHOLD")
    assert hasattr(kr_forensic_core, "PARQUET_TABLES")
    assert hasattr(kr_forensic_core, "data_dir")
