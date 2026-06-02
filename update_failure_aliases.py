"""
Append post-processing aliases for common eval failure predictions (priority 2).

Updates merchant_aliases.csv in place. Used by kestrel_metrics.load_aliases().

Usage:
  python update_failure_aliases.py
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).parent
ALIASES = ROOT / "merchant_aliases.csv"

# predicted_or_variant -> canonical merchant
FAILURE_ALIASES = [
    ("Jackbox", "Jack in the Box"),
    ("GS CTRL & SOUTHERN", "GIRL SCOUTS"),
    ("GS OF THE JERSEY SHORE", "GIRL SCOUTS"),
    ("GIRL SCOUT COOKIES", "GIRL SCOUTS"),
    ("Spyware", "Spotify"),
    ("Shake Shake", "Shake Shack"),
    ("Shakez", "Sheetz"),
    ("CVS CAREPASS", "CVS"),
    ("ORANGE LEAF FROZEN", "Orange Leaf"),
    ("Ferrero Roch", "Ferrero Rocher"),
    ("GrubhubOODFOODBYUZMA", "Grubhub"),
    ("DD STOREKANDAHARAFGHA", "DoorDash"),
    ("DOORDASH & ROUND PIE PIZ", "DoorDash"),
    ("HYUNDAI", "HYUNDAI BLUE LINK"),  # only when expected was BLUE LINK - risky
    ("RAAVI FOODS", "RAAVI NAAN KABAB"),
    ("BCF ETSY UPLIFT", "Etsy"),
    ("CMSVEND", "CMS"),
    ("RVL", "Revolution Clothing"),
    ("Trailblas", "Bass Pro Shops"),
    ("Bigbage", "Big Basket"),
    ("Bose", "BJ's Wholesale Club"),  # ambiguous - skip
]

# Skip ambiguous global corrections
SKIP = {"Bose", "HYUNDAI", "YANKEE", "ACE"}


def main() -> None:
    existing: dict[str, tuple[str, str]] = {}
    if ALIASES.exists():
        with ALIASES.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                alias = row["alias"].strip()
                existing[alias] = (row["canonical"].strip(), row.get("notes", ""))

    added = 0
    for alias, canonical in FAILURE_ALIASES:
        if alias in SKIP:
            continue
        if alias not in existing:
            existing[alias] = (canonical, "failure_alias")
            added += 1
        elif existing[alias][0] != canonical:
            existing[alias] = (canonical, "failure_alias")

    with ALIASES.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["alias", "canonical", "notes"])
        for alias in sorted(existing, key=lambda a: (existing[a][0].lower(), a.lower())):
            canonical, notes = existing[alias]
            writer.writerow([alias, canonical, notes])

    print(f"Updated {ALIASES} (+{added} failure aliases, {len(existing)} total)")


if __name__ == "__main__":
    main()