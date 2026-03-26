# kr-forensic-core

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
pip install kr-forensic-core
```
