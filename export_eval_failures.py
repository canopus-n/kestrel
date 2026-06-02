"""
Export evaluation failures from eval_report.json for labeling review.

Usage:
  python evaluate.py --json eval_report.json   # if needed
  python export_eval_failures.py
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
REPORT = ROOT / "eval_report.json"
OUTPUT = ROOT / "eval_failures.csv"


def classify_pattern(description: str) -> str:
    if description.startswith("PAYPAL DES:INST XFER"):
        return "paypal_inst_xfer"
    if description.startswith("**ID"):
        return "pipe_delimited"
    if re.search(r"#[X\d]{4,}", description) or re.search(r"_\d{2,4}\s", description):
        return "obfuscated_code"
    if description.startswith("*SQ ") or description.startswith("SQ *"):
        return "square_prefix"
    if "DOORDASH" in description or "GRUBHUB" in description:
        return "delivery_platform"
    if "GIRL SCOUT" in description or description.startswith("GS "):
        return "girl_scouts"
    return "other"


def suggest_action(pattern: str, token_f1: float) -> str:
    if pattern == "paypal_inst_xfer":
        return "add_paypal_variants"
    if pattern == "pipe_delimited":
        return "add_pipe_id_variants"
    if pattern == "obfuscated_code":
        return "add_obfuscated_variants"
    if token_f1 >= 0.5:
        return "alias_or_canonicalize"
    return "add_training_variants"


def main() -> None:
    if not REPORT.exists():
        raise SystemExit(f"Missing {REPORT}. Run: python evaluate.py --json eval_report.json")

    report = json.loads(REPORT.read_text(encoding="utf-8"))
    rows: list[dict] = []

    for block in report["sets"]:
        for fail in block.get("failures", []):
            desc = fail["description"]
            pattern = classify_pattern(desc)
            rows.append(
                {
                    "eval_set": block["name"],
                    "pattern": pattern,
                    "suggested_action": suggest_action(pattern, fail.get("token_f1", 0)),
                    "description": desc,
                    "expected": fail["expected"],
                    "predicted": fail["predicted"],
                    "token_f1": fail.get("token_f1", 0),
                }
            )

    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "eval_set",
                "pattern",
                "suggested_action",
                "description",
                "expected",
                "predicted",
                "token_f1",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    by_pattern: dict[str, int] = {}
    for r in rows:
        by_pattern[r["pattern"]] = by_pattern.get(r["pattern"], 0) + 1

    print(f"Wrote {OUTPUT} ({len(rows)} failures)")
    for pattern, count in sorted(by_pattern.items(), key=lambda x: -x[1]):
        print(f"  {pattern}: {count}")


if __name__ == "__main__":
    main()