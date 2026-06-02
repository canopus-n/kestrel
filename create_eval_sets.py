"""
Create frozen held-out evaluation sets from combined_transactions.csv.

Outputs:
  eval_merchant.csv      (~400 merchant rows)
  eval_non_merchant.csv  (~150 non-merchant rows)
  eval_manual.json       (hand-picked regression cases)

These descriptions are excluded from train.py when training.

Usage:
  python create_eval_sets.py
"""

from __future__ import annotations

import csv
import json
import random
from pathlib import Path

ROOT = Path(__file__).parent
COMBINED = ROOT / "combined_transactions.csv"
EVAL_MERCHANT = ROOT / "eval_merchant.csv"
EVAL_NON_MERCHANT = ROOT / "eval_non_merchant.csv"
EVAL_MANUAL = ROOT / "eval_manual.json"

SEED = 42
MERCHANT_EVAL_SIZE = 400
NON_MERCHANT_EVAL_SIZE = 150

from kestrel_metrics import NO_MERCHANT, is_no_merchant

MANUAL_CASES = [
    {"description": "NETFLIX.COM 121 ALBRIGHT WAY LOS GATOS 95032 CA USA", "merchant": "Netflix"},
    {"description": "MCDONALD'S F2548 RT 35 & AMBOY CLIFFWOOD BEA07735 NJ USA", "merchant": "McDonald's"},
    {"description": "WAL-MART #2825 1126 US HIGHWAY 9 OLD BRIDGE 08857 NJ USA", "merchant": "Walmart"},
    {
        "description": "GOOGLE *YOUTUBEPREMIUM1600 AMPHITHEATRE PKWY 650-253-0000 94043 CA USA",
        "merchant": "YouTube Premium",
    },
    {
        "description": "PAYPAL DES:INST XFER ID:LYFTRIDEUS INDN:JENNIFER DAVIS CO ID:PAYPALSI78 WEB",
        "merchant": "Lyft",
    },
    {
        "description": "TRADER_JS_092 07/08 #XXXXX0092 PURCHASE GROCERIES MONROVIA CA",
        "merchant": "Trader Joe's",
    },
    {"description": "GEICO *AUTO ONE GEICO PLAZA 800-841-3000 20076 DC USA", "merchant": "GEICO"},
    {"description": "APPLE.COM/BILL ONE APPLE PARK WAY 866-712-7753 95014 CA USA", "merchant": "Apple"},
    {
        "description": "SHOPRITE HAZLET S1 3150 STATE HIGHWAY 35 HAZLET 07735 NJ USA",
        "merchant": "ShopRite",
    },
    {"description": "NJ EZPASS 375 MCCARTER HIGHWAY NEWARK 07114 NJ USA", "merchant": "NJ E-ZPass"},
    {"description": "ACH DEPOSIT INTERNET TRANSFER FROM ACCOUNT ENDING IN 1986", "merchant": NO_MERCHANT},
    {"description": "DAILY CASH ADJUSTMENT", "merchant": NO_MERCHANT},
]


def load_combined() -> tuple[list[dict], list[dict]]:
    merchants: list[dict] = []
    non_merchants: list[dict] = []
    manual_desc = {c["description"] for c in MANUAL_CASES}

    with COMBINED.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            desc = row["description"].strip()
            merchant = row["merchant"]
            if desc in manual_desc:
                continue
            entry = {"description": desc, "merchant": merchant}
            if is_no_merchant(merchant):
                non_merchants.append(entry)
            else:
                merchants.append(entry)
    return merchants, non_merchants


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["description", "merchant"])
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    if not COMBINED.exists():
        raise SystemExit(f"Missing {COMBINED}")

    rng = random.Random(SEED)
    merchants, non_merchants = load_combined()

    rng.shuffle(merchants)
    rng.shuffle(non_merchants)

    merchant_eval = merchants[:MERCHANT_EVAL_SIZE]
    non_merchant_eval = non_merchants[:NON_MERCHANT_EVAL_SIZE]

    write_csv(EVAL_MERCHANT, merchant_eval)
    write_csv(EVAL_NON_MERCHANT, non_merchant_eval)
    EVAL_MANUAL.write_text(json.dumps(MANUAL_CASES, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote {EVAL_MERCHANT} ({len(merchant_eval)} rows)")
    print(f"Wrote {EVAL_NON_MERCHANT} ({len(non_merchant_eval)} rows)")
    print(f"Wrote {EVAL_MANUAL} ({len(MANUAL_CASES)} rows)")
    print(
        f"Total held-out descriptions: "
        f"{len(merchant_eval) + len(non_merchant_eval) + len(MANUAL_CASES)}"
    )


if __name__ == "__main__":
    main()