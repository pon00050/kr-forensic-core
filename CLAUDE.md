# kr-forensic-core
> Shared constants, schemas, and path conventions for the forensic accounting ecosystem — zero external dependencies.

## Install & Test
```bash
uv sync
uv run pytest tests/ -v
```

## Architecture

Three modules in `kr_forensic_core/`:
- `constants.py` — Beneish threshold, CB/BW flag names, scoring thresholds (all plain Python primitives)
- `paths.py` — `data_dir()` resolves processed data path: `KRFF_DATA_DIR` env var → `<repo_root>/01_Data/processed`
- `schemas.py` — `PARQUET_TABLES` dict: canonical column schemas for all parquet outputs

## Conventions
- Package manager: `uv`
- Build system: hatchling
- Test command: `uv run pytest tests/ -v`
- Zero external dependencies — only stdlib. Adding a dependency here forces it on every consuming repo.

## Key Decisions
- No `src/` layout — flat `kr_forensic_core/` package. Avoids import path complexity given this is a pure-utility library.
- `paths.py` env-var override (`KRFF_DATA_DIR`) allows CI and Docker deployments to redirect data paths without code changes.
- Constants are intentionally not dataclasses/Pydantic — primitives only, so any consuming repo can import without a pydantic dep.

## Known Gaps

| Gap | Why | Status |
|-----|-----|--------|
| No validation of `KRFF_DATA_DIR` path on startup | Low priority — consuming repos validate parquet existence themselves | By design |
