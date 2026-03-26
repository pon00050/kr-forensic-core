"""kr-forensic-core — Shared constants, schemas, and path conventions.

Zero external dependencies. Auto-installs as a dependency of all forensic
accounting ecosystem repos (kr-dart-pipeline, kr-anomaly-scoring,
kr-stat-tests, krff-shell).

Usage:
    from kr_forensic_core import BENEISH_THRESHOLD, FLAG_REPRICING_BELOW_MARKET
    from kr_forensic_core import PARQUET_TABLES, data_dir
    from kr_forensic_core.schemas import BENEISH_SCORES_COLUMNS
"""

from __future__ import annotations

from kr_forensic_core.constants import *  # noqa: F401, F403
from kr_forensic_core.schemas import PARQUET_TABLES  # noqa: F401
from kr_forensic_core.paths import data_dir  # noqa: F401

__version__ = "1.0.0"
