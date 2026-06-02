"""
Normalize merchant labels in combined_transactions.csv before training.

Workflow:
  1. python normalize_merchant_labels.py audit
     -> label_conflicts.csv (clusters with more than one merchant string)

  2. python normalize_merchant_labels.py suggest
     -> merchant_aliases.csv (alias -> canonical; review and edit)

  3. python normalize_merchant_labels.py apply
     -> combined_transactions.csv (backs up prior file to .bak)

Re-run train.py after apply.
"""

from __future__ import annotations

import argparse
import csv
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).parent
INPUT = ROOT / "combined_transactions.csv"
CONFLICTS = ROOT / "label_conflicts.csv"
ALIASES = ROOT / "merchant_aliases.csv"
BACKUP = ROOT / "combined_transactions.csv.bak"


def norm_key(merchant: str) -> str:
    """Cluster key: lowercase alphanumeric only."""
    s = merchant.lower().strip()
    return re.sub(r"[^a-z0-9]+", "", s)


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def pick_canonical(forms: Counter[str]) -> str:
    """
    Default canonical name for a cluster.
    Prefer the most common label; break ties with nicer casing (not ALL CAPS).
    """
    ranked = forms.most_common()
    top_count = ranked[0][1]
    tied = [name for name, count in ranked if count == top_count]

    def score(name: str) -> tuple[int, int, str]:
        # Higher is better: mixed case > ALL CAPS, fewer digits, shorter
        all_caps = name == name.upper() and any(c.isalpha() for c in name)
        return (
            0 if all_caps else 1,
            -sum(c.isdigit() for c in name),
            -len(name),
            name,
        )

    return max(tied, key=score)


def cluster_merchants(rows: list[dict[str, str]]) -> dict[str, Counter[str]]:
    clusters: dict[str, Counter[str]] = defaultdict(Counter)
    for row in rows:
        clusters[norm_key(row["merchant"])][row["merchant"]] += 1
    return clusters


def cmd_audit(rows: list[dict[str, str]]) -> None:
    clusters = cluster_merchants(rows)
    conflicts = {k: v for k, v in clusters.items() if len(v) > 1}

    with CONFLICTS.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["cluster_key", "canonical_suggested", "alias", "row_count", "aliases_in_cluster"]
        )
        for key in sorted(conflicts, key=lambda k: -sum(conflicts[k].values())):
            forms = conflicts[key]
            canonical = pick_canonical(forms)
            alias_list = "; ".join(f"{n} ({c})" for n, c in forms.most_common())
            for alias, count in forms.most_common():
                writer.writerow([key, canonical, alias, count, alias_list])

    print(f"Wrote {CONFLICTS} ({len(conflicts)} conflicting clusters)")


def cmd_suggest(rows: list[dict[str, str]]) -> None:
    clusters = cluster_merchants(rows)
    mapping: dict[str, str] = {}

    for forms in clusters.values():
        canonical = pick_canonical(forms)
        for alias in forms:
            mapping[alias] = canonical

    with ALIASES.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["alias", "canonical", "notes"])
        for alias in sorted(mapping, key=lambda s: (mapping[s].lower(), s.lower())):
            note = "conflict" if mapping[alias] != alias else ""
            writer.writerow([alias, mapping[alias], note])

    conflicts = sum(1 for k, v in clusters.items() if len(v) > 1)
    print(f"Wrote {ALIASES} ({len(mapping)} aliases, {conflicts} clusters had conflicts)")
    print("Edit canonical column for rows you disagree with, then run: apply")


def load_aliases() -> dict[str, str]:
    if not ALIASES.exists():
        raise SystemExit(f"Missing {ALIASES}. Run: python normalize_merchant_labels.py suggest")

    mapping: dict[str, str] = {}
    with ALIASES.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            alias = row["alias"].strip()
            canonical = row["canonical"].strip()
            if alias and canonical:
                mapping[alias] = canonical
    return mapping


def cmd_apply(rows: list[dict[str, str]]) -> None:
    mapping = load_aliases()
    changed = 0
    unknown: Counter[str] = Counter()

    for row in rows:
        merchant = row["merchant"]
        if merchant in mapping:
            new = mapping[merchant]
            if new != merchant:
                changed += 1
            row["merchant"] = new
        else:
            unknown[merchant] += 1

    if unknown:
        print(f"Warning: {len(unknown)} merchant strings not in {ALIASES.name} (left unchanged)")
        for name, count in unknown.most_common(5):
            print(f"  {name!r}: {count} rows")

    if INPUT.exists():
        shutil.copy2(INPUT, BACKUP)
        print(f"Backup: {BACKUP}")

    with INPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["description", "merchant"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Updated {INPUT}: {changed} merchant labels rewritten")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "command",
        choices=["audit", "suggest", "apply"],
        help="audit=conflicts only; suggest=aliases file; apply=rewrite CSV",
    )
    args = parser.parse_args()

    if not INPUT.exists():
        raise SystemExit(f"Missing {INPUT}. Run combine_datasets.py first.")

    rows = load_rows(INPUT)
    print(f"Loaded {len(rows)} rows from {INPUT.name}")

    if args.command == "audit":
        cmd_audit(rows)
    elif args.command == "suggest":
        cmd_suggest(rows)
    else:
        cmd_apply(rows)


if __name__ == "__main__":
    main()