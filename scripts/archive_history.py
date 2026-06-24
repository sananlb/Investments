#!/usr/bin/env python3
"""
Append-only history archive for the sector valuation pipeline.

Problem (see data/market_quotes/pipeline_audit.md): point-in-time history is
scattered and partly lost. Undated current_summary snapshots get overwritten on
every update_all run, the 5Y NORM is never versioned (so a future recompute
silently destroys the norm a past score was built on), and there is no single
long-lived table of "date x sector x metric x value". This script fixes the
STORAGE side only: it reads files that already exist locally and writes a
durable archive. It performs NO network requests and runs NO collector scripts,
so it is safe to run while backfill_history.py is collecting in the background.

What it does (all local, read-only on the source files):

1. SINGLE APPEND-ONLY POINTS ARCHIVE
   data/market_quotes/archive/sector_metrics_archive.csv
   Schema: snapshot_date, sector, slug, metric, value, n_companies, status,
           source_file, archived_at
   Sources folded in:
     - fyn_<slug>_current_<YYYYMMDD>_summary.csv  (dated snapshots)
     - fyn_<slug>_current_summary.csv             (undated "today" snapshots)
     - sector_scores*.csv                         (historical anchor points,
       which include dates that the dated summaries do not cover)
   Append-only: a row is keyed by (snapshot_date, sector, metric, source_file).
   On re-run, rows already present are skipped; only genuinely new rows are
   appended. The existing archive file is never rewritten or reordered.

2. NORM VERSIONING
   Copies each fyn_<slug>_norm_summary.csv to
   data/market_quotes/archive/norms/fyn_<slug>_norm_<YYYYMMDD>_summary.csv
   so the norm a past score used is preserved. Idempotent: if a version for the
   same slug+date already exists with identical content it is left untouched.

3. RAW INDEX (lightweight)
   data/market_quotes/archive/raw_index.csv lists the company-level "source of
   truth" raw files (fyn_<slug>_current_<date>.csv detail, fyn_<slug>_norm.csv)
   without duplicating their contents: slug, file, type, date, n_rows. The raw
   files themselves stay where they are; the archive README marks them as the
   authoritative raw source.

Arguments:
  --archive-dir DIR   default data/market_quotes/archive
  --source-dir  DIR   default data/market_quotes (where the fyn_* files live)
  --dry-run           report what WOULD be added/versioned, write nothing.

This script never invents numbers. If a snapshot date cannot be determined for a
summary row, that row is reported and skipped rather than guessed.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Paths and constants
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SOURCE_DIR = REPO_ROOT / "data" / "market_quotes"
DEFAULT_ARCHIVE_DIR = DEFAULT_SOURCE_DIR / "archive"

ARCHIVE_CSV_NAME = "sector_metrics_archive.csv"
RAW_INDEX_NAME = "raw_index.csv"
NORMS_SUBDIR = "norms"

ARCHIVE_FIELDS = [
    "snapshot_date",
    "sector",
    "slug",
    "metric",
    "value",
    "n_companies",
    "status",
    "source_file",
    "archived_at",
]

RAW_INDEX_FIELDS = ["slug", "file", "type", "date", "n_rows"]

# slug -> display sector name. Kept in sync with scripts/update_all.py SECTORS.
# Imported at runtime when available; this literal is the offline fallback so
# the archiver never needs to import a module that may touch the network.
SECTORS: Dict[str, str] = {
    "banks": "Banks",
    "energy": "Energy",
    "telecom": "Telecom & Streaming",
    "delivery_logistics": "Delivery & Logistics",
    "insurance": "Insurance",
    "utilities": "Utilities",
    "mining": "Mining",
    "drugs": "Drugs",
    "commodities": "Commodities",
    "semis": "Semiconductors",
    "food": "Food & Staples",
    "technology": "Technology",
    "agriculture_chemicals": "Agriculture & Chemicals",
    "consumer_discretionary": "Consumer Discretionary",
    "medical_services": "Medtech & Life Science Tools",
    "solar": "Solar",
    "reit": "REIT",
}

# reverse: display name -> slug, for parsing sector_scores* (which carry the
# display name, not the slug).
SECTOR_NAME_TO_SLUG: Dict[str, str] = {name: slug for slug, name in SECTORS.items()}

# Match the "...as of 2026-06-07..." date inside a summary comment.
_AS_OF_RE = re.compile(r"as of (\d{4}-\d{2}-\d{2})")
# Match the YYYYMMDD chunk in a dated current/norm filename.
_DATED_STEM_RE = re.compile(r"_current_(\d{8})_summary\.csv$")


def _today_compact() -> str:
    return dt.date.today().strftime("%Y%m%d")


def _ymd_to_iso(ymd: str) -> str:
    """20260510 -> 2026-05-10."""
    return f"{ymd[0:4]}-{ymd[4:6]}-{ymd[6:8]}"


def _slug_from_fyn(name: str, infix: str) -> Optional[str]:
    """Extract <slug> from a 'fyn_<slug>_<infix>...' filename."""
    if not name.startswith("fyn_"):
        return None
    rest = name[len("fyn_"):]
    idx = rest.find(infix)
    if idx <= 0:
        return None
    return rest[:idx]


# ---------------------------------------------------------------------------
# Reading existing archive (for append-only dedup)
# ---------------------------------------------------------------------------


def load_existing_keys(archive_csv: Path) -> set:
    """Return the set of (snapshot_date, sector, metric, source_file) already
    present in the points archive, so we never write a duplicate."""
    keys = set()
    if not archive_csv.exists():
        return keys
    with archive_csv.open("r", newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            keys.add(
                (
                    row.get("snapshot_date", ""),
                    row.get("sector", ""),
                    row.get("metric", ""),
                    row.get("source_file", ""),
                )
            )
    return keys


# ---------------------------------------------------------------------------
# Collectors: produce archive rows from the various source files
# ---------------------------------------------------------------------------


def _summary_snapshot_date(path: Path, rows: List[dict]) -> Optional[str]:
    """Determine the snapshot date for a *_summary.csv file.

    Dated files carry the date in the filename; undated files carry it in the
    'as of YYYY-MM-DD' part of any row comment. Returns ISO date or None.
    """
    m = _DATED_STEM_RE.search(path.name)
    if m:
        return _ymd_to_iso(m.group(1))
    for row in rows:
        comment = row.get("comment", "") or ""
        hit = _AS_OF_RE.search(comment)
        if hit:
            return hit.group(1)
    return None


def collect_from_summaries(source_dir: Path) -> Tuple[List[dict], List[str]]:
    """Rows from fyn_<slug>_current_*summary.csv (dated and undated)."""
    out: List[dict] = []
    warnings: List[str] = []
    archived_at = dt.datetime.now().isoformat(timespec="seconds")

    summary_paths = sorted(source_dir.glob("fyn_*_current*summary.csv"))
    for path in summary_paths:
        dated = bool(_DATED_STEM_RE.search(path.name))
        if dated:
            slug = _slug_from_fyn(path.name, "_current_")
        else:
            slug = _slug_from_fyn(path.name, "_current_summary.csv")
        if not slug:
            warnings.append(f"could not parse slug from {path.name}; skipped")
            continue
        sector = SECTORS.get(slug, slug)

        with path.open("r", newline="", encoding="utf-8") as fh:
            rows = list(csv.DictReader(fh))

        snapshot_date = _summary_snapshot_date(path, rows)
        if not snapshot_date:
            warnings.append(f"no snapshot date found in {path.name}; skipped")
            continue

        for row in rows:
            metric = (row.get("metric") or "").strip()
            if not metric:
                continue
            out.append(
                {
                    "snapshot_date": snapshot_date,
                    "sector": sector,
                    "slug": slug,
                    "metric": metric,
                    "value": (row.get("value") or "").strip(),
                    "n_companies": (row.get("n_companies") or "").strip(),
                    "status": (row.get("status") or "").strip(),
                    "source_file": path.name,
                    "archived_at": archived_at,
                }
            )
    return out, warnings


def collect_from_sector_scores(source_dir: Path) -> Tuple[List[dict], List[str]]:
    """Rows from sector_scores.csv (and any sector_scores*.csv variant).

    sector_scores.csv carries the historical anchor points (e.g. the monthly
    2026-02..2026-05 series) that the dated summary files do not cover, so it is
    an important history source. Each row already holds a per-metric
    current_value; we archive that as the metric 'value'. Preview variants use a
    different layout (one row per sector, metric='sector_score', no per-metric
    current value) and carry no new per-metric points, so they are skipped with
    a note rather than mis-parsed.
    """
    out: List[dict] = []
    warnings: List[str] = []
    archived_at = dt.datetime.now().isoformat(timespec="seconds")

    score_paths = sorted(source_dir.glob("sector_scores*.csv"))
    for path in score_paths:
        with path.open("r", newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            fieldnames = reader.fieldnames or []
            # Only the detailed per-metric layout has both an anchor_date and a
            # current_value column. Preview tables lack these.
            if "current_value" not in fieldnames or "anchor_date" not in fieldnames:
                warnings.append(
                    f"{path.name}: not a per-metric score table "
                    f"(no anchor_date/current_value); skipped"
                )
                continue
            for row in reader:
                metric = (row.get("metric") or "").strip()
                snapshot_date = (row.get("anchor_date") or "").strip()
                sector = (row.get("sector") or "").strip()
                if not (metric and snapshot_date and sector):
                    continue
                slug = SECTOR_NAME_TO_SLUG.get(sector, "")
                out.append(
                    {
                        "snapshot_date": snapshot_date,
                        "sector": sector,
                        "slug": slug,
                        "metric": metric,
                        "value": (row.get("current_value") or "").strip(),
                        "n_companies": "",  # not present in score rows
                        "status": (row.get("status") or "").strip(),
                        "source_file": path.name,
                        "archived_at": archived_at,
                    }
                )
    return out, warnings


# ---------------------------------------------------------------------------
# Norm versioning
# ---------------------------------------------------------------------------


def _norm_version_date(path: Path) -> str:
    """Date stamp for a norm version. Norm summaries carry no point-in-time date
    of their own, so use the source file's modification date (the day the norm
    was built); fall back to today if unreadable."""
    try:
        mtime = dt.date.fromtimestamp(path.stat().st_mtime)
        return mtime.strftime("%Y%m%d")
    except OSError:
        return _today_compact()


def version_norms(
    source_dir: Path, archive_dir: Path, dry_run: bool
) -> Tuple[List[str], List[str]]:
    """Copy each fyn_<slug>_norm_summary.csv into archive/norms/ with a date
    stamp. Idempotent: skip if an identical dated version already exists."""
    norms_dir = archive_dir / NORMS_SUBDIR
    created: List[str] = []
    skipped: List[str] = []

    norm_paths = sorted(source_dir.glob("fyn_*_norm_summary.csv"))
    for path in norm_paths:
        slug = _slug_from_fyn(path.name, "_norm_summary.csv")
        if not slug:
            continue
        stamp = _norm_version_date(path)
        dest = norms_dir / f"fyn_{slug}_norm_{stamp}_summary.csv"
        content = path.read_text(encoding="utf-8")
        if dest.exists() and dest.read_text(encoding="utf-8") == content:
            skipped.append(dest.name)
            continue
        if dest.exists():
            # Same day, different content: keep the first version untouched
            # (append-only spirit) and record under a content-disambiguated name.
            alt = norms_dir / f"fyn_{slug}_norm_{stamp}_v2_summary.csv"
            n = 2
            while alt.exists() and alt.read_text(encoding="utf-8") != content:
                n += 1
                alt = norms_dir / f"fyn_{slug}_norm_{stamp}_v{n}_summary.csv"
            if alt.exists():
                skipped.append(alt.name)
                continue
            dest = alt
        if not dry_run:
            norms_dir.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding="utf-8")
        created.append(dest.name)
    return created, skipped


# ---------------------------------------------------------------------------
# Raw index
# ---------------------------------------------------------------------------


def _count_data_rows(path: Path) -> int:
    try:
        with path.open("r", newline="", encoding="utf-8") as fh:
            n = sum(1 for _ in csv.reader(fh))
        return max(n - 1, 0)  # minus header
    except OSError:
        return 0


def build_raw_index(source_dir: Path) -> List[dict]:
    """Index of company-level raw files (source of truth), not their contents."""
    rows: List[dict] = []

    # Dated current detail files: fyn_<slug>_current_<YYYYMMDD>.csv
    dated_detail_re = re.compile(r"^fyn_(.+)_current_(\d{8})\.csv$")
    for path in sorted(source_dir.glob("fyn_*_current_*.csv")):
        m = dated_detail_re.match(path.name)
        if not m:
            continue
        rows.append(
            {
                "slug": m.group(1),
                "file": path.name,
                "type": "current",
                "date": _ymd_to_iso(m.group(2)),
                "n_rows": _count_data_rows(path),
            }
        )

    # Norm detail files: fyn_<slug>_norm.csv
    for path in sorted(source_dir.glob("fyn_*_norm.csv")):
        slug = _slug_from_fyn(path.name, "_norm.csv")
        if not slug:
            continue
        rows.append(
            {
                "slug": slug,
                "file": path.name,
                "type": "norm",
                "date": dt.date.fromtimestamp(path.stat().st_mtime).isoformat(),
                "n_rows": _count_data_rows(path),
            }
        )

    rows.sort(key=lambda r: (r["slug"], r["type"], r["date"]))
    return rows


# ---------------------------------------------------------------------------
# README
# ---------------------------------------------------------------------------

README_TEXT = """\
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
"""


# ---------------------------------------------------------------------------
# Writers
# ---------------------------------------------------------------------------


def append_points(archive_csv: Path, new_rows: List[dict], dry_run: bool) -> None:
    if dry_run or not new_rows:
        return
    archive_csv.parent.mkdir(parents=True, exist_ok=True)
    write_header = not archive_csv.exists()
    with archive_csv.open("a", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=ARCHIVE_FIELDS)
        if write_header:
            writer.writeheader()
        for row in new_rows:
            writer.writerow(row)


def write_raw_index(index_csv: Path, rows: List[dict], dry_run: bool) -> None:
    if dry_run:
        return
    index_csv.parent.mkdir(parents=True, exist_ok=True)
    with index_csv.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=RAW_INDEX_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def write_readme(readme_path: Path, dry_run: bool) -> None:
    if dry_run:
        return
    readme_path.parent.mkdir(parents=True, exist_ok=True)
    readme_path.write_text(README_TEXT, encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Fold local sector valuation readings into a single append-only "
            "archive and version the 5Y norms. Local only; no network."
        )
    )
    parser.add_argument(
        "--archive-dir",
        type=Path,
        default=DEFAULT_ARCHIVE_DIR,
        help="Archive output directory (default data/market_quotes/archive).",
    )
    parser.add_argument(
        "--source-dir",
        type=Path,
        default=DEFAULT_SOURCE_DIR,
        help="Where the fyn_* / sector_scores* files live "
        "(default data/market_quotes).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report what would be added/versioned; write nothing.",
    )
    args = parser.parse_args()

    source_dir: Path = args.source_dir
    archive_dir: Path = args.archive_dir
    archive_csv = archive_dir / ARCHIVE_CSV_NAME

    if not source_dir.exists():
        raise SystemExit(f"source dir not found: {source_dir}")

    print(f"Source : {source_dir}")
    print(f"Archive: {archive_dir}{'  (DRY RUN)' if args.dry_run else ''}")
    print()

    # 1) Points archive (append-only).
    existing_keys = load_existing_keys(archive_csv)
    summary_rows, sum_warn = collect_from_summaries(source_dir)
    score_rows, score_warn = collect_from_sector_scores(source_dir)
    candidate_rows = summary_rows + score_rows

    # Dedup against what is already stored AND within this batch (a metric can
    # appear in both an undated summary and sector_scores for the same date;
    # the dedup key keeps them distinct only when source_file differs, which is
    # intended — different provenance, kept separately).
    new_rows: List[dict] = []
    batch_keys = set()
    for row in candidate_rows:
        key = (row["snapshot_date"], row["sector"], row["metric"], row["source_file"])
        if key in existing_keys or key in batch_keys:
            continue
        batch_keys.add(key)
        new_rows.append(row)

    append_points(archive_csv, new_rows, args.dry_run)

    src_summary_files = len(set(r["source_file"] for r in summary_rows))
    src_score_files = len(set(r["source_file"] for r in score_rows))
    print("[1] Points archive  ->", archive_csv.name)
    print(f"    candidate readings : {len(candidate_rows)} "
          f"(summaries={len(summary_rows)} from {src_summary_files} files, "
          f"scores={len(score_rows)} from {src_score_files} files)")
    print(f"    already in archive : {len(existing_keys)} keys")
    print(f"    NEW appended       : {len(new_rows)}"
          f"{' (dry-run, not written)' if args.dry_run else ''}")
    for w in sum_warn + score_warn:
        print(f"    note: {w}")

    # 2) Norm versioning.
    created, skipped = version_norms(source_dir, archive_dir, args.dry_run)
    print()
    print("[2] Norm versioning ->", f"{archive_dir.name}/{NORMS_SUBDIR}/")
    print(f"    NEW versions       : {len(created)}"
          f"{' (dry-run, not written)' if args.dry_run else ''}")
    print(f"    already versioned  : {len(skipped)}")
    for name in created:
        print(f"      + {name}")

    # 3) Raw index.
    raw_rows = build_raw_index(source_dir)
    write_raw_index(archive_dir / RAW_INDEX_NAME, raw_rows, args.dry_run)
    n_current = sum(1 for r in raw_rows if r["type"] == "current")
    n_norm = sum(1 for r in raw_rows if r["type"] == "norm")
    print()
    print("[3] Raw index       ->", RAW_INDEX_NAME)
    print(f"    indexed raw files  : {len(raw_rows)} "
          f"(current={n_current}, norm={n_norm})"
          f"{' (dry-run, not written)' if args.dry_run else ''}")

    # README.
    write_readme(archive_dir / "README.md", args.dry_run)
    print()
    print("[4] README          ->", "README.md",
          "(dry-run, not written)" if args.dry_run else "(written)")

    print()
    print("Done. No network was contacted; only local files were read/written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
