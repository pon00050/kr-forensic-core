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


---

**Working notes** (regulatory analysis, legal compliance research, or anything else not appropriate for this public repo) belong in the gitignored working directory of the coordination hub. Engineering docs (API patterns, test strategies, run logs) stay here.

---

## NEVER commit to this repo

This repository is **public**. Before staging or writing any new file, check the list below. If the content matches any item, route it to the gitignored working directory of the coordination hub instead, NOT to this repo.

**Hard NO list:**

1. **Any API key, token, or credential — even a truncated fingerprint.** This includes Anthropic key fingerprints (sk-ant-...), AWS keys (AKIA...), GitHub tokens (ghp_...), DART/SEIBRO/KFTC API keys, FRED keys. Even partial / display-truncated keys (e.g. "sk-ant-api03-...XXXX") leak the org-to-key linkage and must not be committed.
2. **Payment / billing data of any kind.** Card numbers (full or last-four), invoice IDs, receipt numbers, order numbers, billing-portal URLs, Stripe/Anthropic/PayPal account states, monthly-spend caps, credit balances.
3. **Vendor support correspondence.** Subject lines, body text, ticket IDs, or summaries of correspondence with Anthropic / GitHub / Vercel / DART / any vendor's support team.
4. **Named third-party outreach targets.** Specific company names, hedge-fund names, audit-firm names, regulator-individual names appearing in a planning, pitch, or outreach context. Engineering content discussing Korean financial institutions in a neutral domain context (e.g. "DART is the FSS disclosure system") is fine; planning text naming them as a sales target is not.
5. **Commercial-positioning memos.** Documents discussing buyer segments, monetization models, pricing strategy, competitor analysis, market positioning, or go-to-market plans. Research methodology and technical roadmaps are fine; commercial strategy is not.
6. **Files matching the leak-prevention .gitignore patterns** (*_prep.md, *_billing*, *_outreach*, *_strategy*, *_positioning*, *_pricing*, *_buyer*, *_pitch*, product_direction.md, etc.). If you find yourself wanting to write a file with one of these names, that is a signal that the content belongs in the hub working directory.

**When in doubt:** put the content in the hub working directory (gitignored), not this repo. It is always safe to add later. It is expensive to remove after force-pushing — orphaned commits remain resolvable on GitHub for weeks.

GitHub Push Protection is enabled on this repo and will reject pushes containing well-known credential patterns. That is a backstop, not the primary defense — write-time discipline is.
