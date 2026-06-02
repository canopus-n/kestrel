"""
Test the trained Kestrel model on custom inputs or evaluation sets.

Usage:
    python test.py --input "MCDONALD'S F2548 RT 35 & AMBOY CLIFFWOOD BEA07735 NJ USA"
    python test.py --ofx "/path/to/file.ofx"
    python test.py --eval              # run held-out eval sets (see evaluate.py)
    python test.py                     # manual regression cases
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

import torch
from transformers import AutoTokenizer, T5ForConditionalGeneration

from kestrel_metrics import (
    exact_match,
    is_no_merchant,
    load_aliases,
    normalize_prediction,
    normalized_match,
)

PREFIX = "extract merchant: "


def load_model(model_path: str = "./output/final"):
    path = Path(model_path)
    if not path.exists():
        print(f"Error: Model not found at {path}")
        print("Run train.py first.")
        sys.exit(1)

    tokenizer = AutoTokenizer.from_pretrained("t5-small")
    model = T5ForConditionalGeneration.from_pretrained(path)
    model.eval()

    if torch.backends.mps.is_available():
        model = model.to("mps")
    elif torch.cuda.is_available():
        model = model.to("cuda")

    return model, tokenizer


def predict(model, tokenizer, transaction: str) -> str:
    input_text = PREFIX + transaction
    inputs = tokenizer(input_text, return_tensors="pt", max_length=128, truncation=True)
    device = next(model.parameters()).device
    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=64)

    return normalize_prediction(tokenizer.decode(outputs[0], skip_special_tokens=True))


def parse_ofx(file_path: str) -> list[tuple[str, float]]:
    content = Path(file_path).read_text(errors="replace")
    transactions = []

    for block in content.split("<STMTTRN>")[1:]:
        amount_match = re.search(r"<TRNAMT>([^<\n]+)", block)
        name_match = re.search(r"<NAME>([^<\n]+)", block)

        if amount_match and name_match:
            amount = float(amount_match.group(1).strip())
            name = name_match.group(1).strip()
            name = name.replace("&amp;", "&").replace("&apos;", "'")
            transactions.append((name, amount))

    return transactions


def format_expected(merchant: str) -> str:
    if is_no_merchant(merchant):
        return "(empty)"
    return merchant


def run_manual_tests(model, tokenizer, model_path: str) -> None:
    import json

    manual_path = Path(__file__).parent / "eval_manual.json"
    if manual_path.exists():
        test_cases = [
            (row["description"], row["merchant"])
            for row in json.loads(manual_path.read_text(encoding="utf-8"))
        ]
    else:
        test_cases = [
            ("NETFLIX.COM 121 ALBRIGHT WAY LOS GATOS 95032 CA USA", "Netflix"),
            ("MCDONALD'S F2548 RT 35 & AMBOY CLIFFWOOD BEA07735 NJ USA", "McDonald's"),
            ("WAL-MART #2825 1126 US HIGHWAY 9 OLD BRIDGE 08857 NJ USA", "Walmart"),
            (
                "GOOGLE *YOUTUBEPREMIUM1600 AMPHITHEATRE PKWY 650-253-0000 94043 CA USA",
                "YouTube Premium",
            ),
            (
                "PAYPAL DES:INST XFER ID:LYFTRIDEUS INDN:JENNIFER DAVIS CO ID:PAYPALSI78 WEB",
                "Lyft",
            ),
            (
                "TRADER_JS_092 07/08 #XXXXX0092 PURCHASE GROCERIES MONROVIA CA",
                "Trader Joe's",
            ),
            ("GEICO *AUTO ONE GEICO PLAZA 800-841-3000 20076 DC USA", "GEICO"),
            ("APPLE.COM/BILL ONE APPLE PARK WAY 866-712-7753 95014 CA USA", "Apple"),
            (
                "SHOPRITE HAZLET S1 3150 STATE HIGHWAY 35 HAZLET 07735 NJ USA",
                "ShopRite",
            ),
            ("NJ EZPASS 375 MCCARTER HIGHWAY NEWARK 07114 NJ USA", "NJ E-ZPass"),
            ("ACH DEPOSIT INTERNET TRANSFER FROM ACCOUNT ENDING IN 1986", " "),
            ("DAILY CASH ADJUSTMENT", " "),
        ]

    aliases = load_aliases()
    print(f"\n{'TRANSACTION':<62} {'PREDICTED':<20} {'EXPECTED'}")
    print("-" * 100)

    exact = norm = 0
    for tx, expected in test_cases:
        predicted = predict(model, tokenizer, tx)
        ex_ok = exact_match(predicted, expected, aliases)
        nm_ok = normalized_match(predicted, expected, aliases)
        mark = "✓" if nm_ok else "✗"
        truncated = tx[:59]
        pred_disp = predicted or "(empty)"
        print(f"{mark} {truncated:<60} {pred_disp:<20} {format_expected(expected)}")
        exact += int(ex_ok)
        norm += int(nm_ok)

    n = len(test_cases)
    print(f"\nExact match:      {exact}/{n} ({100 * exact / n:.0f}%)")
    print(f"Normalized match: {norm}/{n} ({100 * norm / n:.0f}%)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Test Kestrel merchant extraction")
    parser.add_argument("--input", "-i", type=str, help="Single transaction string to test")
    parser.add_argument("--ofx", type=str, help="Path to OFX file to test")
    parser.add_argument("--eval", action="store_true", help="Run full evaluate.py on held-out sets")
    parser.add_argument("--model", type=str, default="./output/final", help="Model path")
    args = parser.parse_args()

    if args.eval:
        cmd = [sys.executable, str(Path(__file__).parent / "evaluate.py"), "--model", args.model]
        raise SystemExit(subprocess.call(cmd))

    model, tokenizer = load_model(args.model)

    if args.input:
        result = predict(model, tokenizer, args.input)
        print(f"Input:    {args.input}")
        print(f"Merchant: {result or '(empty)'}")
        return

    if args.ofx:
        transactions = parse_ofx(args.ofx)
        print(f"\n{'TRANSACTION':<62} {'MERCHANT'}")
        print("-" * 90)
        for name, _amount in transactions:
            merchant = predict(model, tokenizer, name) or "(empty)"
            print(f"{name[:59]:<62} {merchant}")
        print(f"\nTotal: {len(transactions)} transactions")
        return

    run_manual_tests(model, tokenizer, args.model)


if __name__ == "__main__":
    main()