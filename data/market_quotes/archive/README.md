# History archive (`data/market_quotes/archive/`)

Durable, **append-only** store of every point-in-time sector valuation reading,
plus versioned 5Y norms. Built by `scripts/archive_history.py`, which reads only
files that already exist locally and performs **no network requests** — it is
safe to run at any time, including while a backfill is collecting.

Why this exists: the live pipeline overwrites undated `*_current_summary.csv`
snapshots on every run and never versions the 5Y norm, so history leaks away
(see `../pipeline_audit.md`). This archive is the place where nothing is lost.

## What is where

- **`sector_metrics_archive.csv`** — the single long-lived points table.
  Columns: `snapshot_date, sector, slug, metric, value, n_companies, status,
  source_file, archived_at`. One row per (date, sector, metric) observation,
  folded in from:
  - dated snapshots `fyn_<slug>_current_<YYYYMMDD>_summary.csv`
  - undated snapshots `fyn_<slug>_current_summary.csv` (date read from the
    "... as of YYYY-MM-DD" comment)
  - `sector_scores*.csv` (the historical anchor series; carries dates the dated
    snapshots do not cover)

- **`norms/fyn_<slug>_norm_<YYYYMMDD>_summary.csv`** — dated copies of each 5Y
  norm summary, so a past score can always be tied to the exact norm it used.
  The date stamp is the build date (source file mtime).

- **`raw_index.csv`** — a lightweight pointer index (no data copied) to the
  company-level raw files that remain the **source of truth**:
  `fyn_<slug>_current_<date>.csv` (per-company current multiples) and
  `fyn_<slug>_norm.csv` (per-company FY history). Columns: `slug, file, type,
  date, n_rows`.

## Append-only guarantees

- The points archive is **never rewritten or reordered**. New rows are only
  appended. Dedup key: `(snapshot_date, sector, metric, source_file)`. Re-running
  the archiver adds only genuinely new readings and skips everything already
  stored.
- Norm versions are **idempotent**: an existing dated version with identical
  content is left untouched; same-day different content is saved alongside under
  a `_vN` suffix rather than overwriting.
- Nothing here is overwritten by the live collectors — this directory is written
  only by `archive_history.py`.

## Source of truth for raw company-level data

The per-company multiples are **not duplicated** into this archive. The
authoritative raw files are the `fyn_<slug>_current_<date>.csv` (detail) and
`fyn_<slug>_norm.csv` files in `../` (`data/market_quotes/`). Use
`raw_index.csv` to locate them quickly.

## Rebuilding / extending

```
python3 scripts/archive_history.py            # fold in any new local readings
python3 scripts/archive_history.py --dry-run  # preview, write nothing
```
