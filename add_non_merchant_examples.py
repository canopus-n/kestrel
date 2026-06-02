"""
Add non-merchant transaction examples to combined_transactions.csv.

Sources (public / open):
  - HuggingFace: DoDataThings/us-bank-transaction-categories
    (Transfer + Fees categories — synthetic US bank statement text)

Label: single space ' ' (empty merchant target for T5 training).

Usage:
  python add_non_merchant_examples.py          # merge new rows
  python add_non_merchant_examples.py --dry-run # preview counts only
"""

from __future__ import annotations

import argparse
import csv
import shutil
from pathlib import Path

from datasets import load_dataset

ROOT = Path(__file__).parent
COMBINED = ROOT / "combined_transactions.csv"
BACKUP = ROOT / "combined_transactions.csv.bak"
NO_MERCHANT = " "

HF_DATASET = "DoDataThings/us-bank-transaction-categories"
HF_CATEGORIES = ("Transfer", "Fees")

# Income lines that are not employer-branded purchases
INCOME_PATTERNS = (
    "interest payment",
    "statement credit",
    "remote online deposit",
    "tax refund",
    "dividend",
    "social security",
    "unemployment",
    "child tax credit",
    "zelle payment from",
    "zelle payment to",
    "cash app cashout",
    "venmo cashout",
    "direct deposit",
)


def load_combined() -> dict[str, str]:
    rows: dict[str, str] = {}
    with COMBINED.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            desc = row["description"].strip()
            if desc:
                rows[desc] = row["merchant"]
    return rows


def is_no_merchant_label(merchant: str) -> bool:
    return not merchant or merchant == NO_MERCHANT


def fetch_public_examples() -> dict[str, str]:
    print(f"Loading {HF_DATASET}...")
    ds = load_dataset(HF_DATASET, split="train")
    out: dict[str, str] = {}

    for row in ds:
        category = row["category"]
        desc = row["description"].strip()
        if not desc:
            continue

        if category in HF_CATEGORIES:
            out[desc] = NO_MERCHANT
            continue

        if category == "Income":
            lower = desc.lower()
            if any(p in lower for p in INCOME_PATTERNS):
                out[desc] = NO_MERCHANT

    print(f"  Collected {len(out)} unique descriptions from HuggingFace")
    return out


def merge(public: dict[str, str], existing: dict[str, str]) -> tuple[int, int, int]:
    added = 0
    updated = 0
    skipped = 0

    for desc, label in public.items():
        if desc not in existing:
            existing[desc] = label
            added += 1
        elif is_no_merchant_label(existing[desc]):
            if existing[desc] != label:
                existing[desc] = label
                updated += 1
        else:
            skipped += 1

    return added, updated, skipped


def write_combined(rows: dict[str, str]) -> None:
    items = sorted(rows.items(), key=lambda x: x[0])
    with COMBINED.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["description", "merchant"])
        for desc, merchant in items:
            writer.writerow([desc, merchant])


def count_no_merchant(rows: dict[str, str]) -> int:
    return sum(1 for m in rows.values() if is_no_merchant_label(m))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print stats without writing combined_transactions.csv",
    )
    args = parser.parse_args()

    if not COMBINED.exists():
        raise SystemExit(f"Missing {COMBINED}. Run combine_datasets.py first.")

    existing = load_combined()
    before_empty = count_no_merchant(existing)
    print(f"Existing rows: {len(existing)} ({before_empty} non-merchant)")

    public = fetch_public_examples()
    added, updated, skipped = merge(public, existing)
    after_empty = count_no_merchant(existing)

    print(f"Would add: {added}, update: {updated}, skip (has merchant): {skipped}")
    print(f"Non-merchant total: {before_empty} -> {after_empty}")

    if args.dry_run:
        return

    if added or updated:
        shutil.copy2(COMBINED, BACKUP)
        print(f"Backup: {BACKUP}")
        write_combined(existing)
        print(f"Wrote {COMBINED} ({len(existing)} rows)")
    else:
        print("No changes needed.")


if __name__ == "__main__":
    main()