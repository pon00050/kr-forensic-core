"""paths.py — Data directory convention for the forensic accounting ecosystem.

Reads KRFF_DATA_DIR environment variable. Falls back to a sensible default
relative to the calling repo's root if the env var is not set.

Zero external dependencies (stdlib only).
"""

from __future__ import annotations

import os
from pathlib import Path


def data_dir(repo_root: Path | str | None = None) -> Path:
    """Return the processed data directory.

    Resolution order:
    1. KRFF_DATA_DIR environment variable (absolute path)
    2. <repo_root>/01_Data/processed  (if repo_root is provided)
    3. Raises ValueError (caller must provide one of the above)
    """
    env_val = os.environ.get("KRFF_DATA_DIR")
    if env_val:
        return Path(env_val)
    if repo_root is not None:
        return Path(repo_root) / "01_Data" / "processed"
    raise ValueError(
        "Cannot determine data directory: set KRFF_DATA_DIR or pass repo_root."
    )


__all__ = ["data_dir"]
