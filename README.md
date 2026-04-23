# kr-forensic-core

**[Read the full write-up →](https://ronanwrites.vercel.app/manuals/forensic-platform-architecture)**

Shared constants, schemas, and path conventions for the Korean forensic accounting ecosystem.

Zero external dependencies. Auto-installs as a transitive dependency of:
- `kr-dart-pipeline` — ETL from DART/KRX/SEIBRO
- `kr-anomaly-scoring` — CB/BW + timing + network scoring
- `kr-stat-tests` — Methodology validation suite
- `krff-shell` — CLI + report delivery layer

## Usage

```python
from kr_forensic_core import BENEISH_THRESHOLD, FLAG_REPRICING_BELOW_MARKET
from kr_forensic_core import PARQUET_TABLES, data_dir
from kr_forensic_core.schemas import BENEISH_SCORES_COLUMNS
```

## Install

```bash
uv add git+https://github.com/pon00050/kr-forensic-core
```
