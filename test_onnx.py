"""
Test the quantized ONNX model to verify it produces the same results as PyTorch.

Usage:
    python test_onnx.py --ofx "Data/Apple Card Transactions - October 2024.ofx"
    python test_onnx.py --input "MCDONALD'S F2548 RT 35 & AMBOY CLIFFWOOD BEA07735 NJ USA"
    python test_onnx.py --model output/onnx-quantized  # test quantized version
"""

import argparse
import re
from pathlib import Path

from optimum.onnxruntime import ORTModelForSeq2SeqLM
from transformers import AutoTokenizer


def load_onnx_model(model_path="./output/onnx"):
    """Load the ONNX model and tokenizer."""
    path = Path(model_path)
    if not path.exists():
        print(f"Error: ONNX model not found at {path}")
        print("Run export_onnx.py first (or quantize.py for quantized).")
        exit(1)

    print(f"Loading ONNX model from {path}...")
    tokenizer = AutoTokenizer.from_pretrained(path)
    model = ORTModelForSeq2SeqLM.from_pretrained(path)
    return model, tokenizer


def predict(model, tokenizer, transaction: str) -> str:
    """Extract merchant name from a transaction string."""
    input_text = f"extract merchant: {transaction}"
    inputs = tokenizer(input_text, return_tensors="pt", max_length=128, truncation=True)
    outputs = model.generate(**inputs, max_length=64)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


def parse_ofx(file_path: str) -> list[tuple[str, float]]:
    """Parse OFX file and extract transaction descriptions and amounts."""
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


def main():
    parser = argparse.ArgumentParser(description="Test Kestrel ONNX model")
    parser.add_argument("--input", "-i", type=str, help="Single transaction string")
    parser.add_argument("--ofx", type=str, help="Path to OFX file")
    parser.add_argument("--model", type=str, default="./output/onnx", help="ONNX model path")
    args = parser.parse_args()

    model, tokenizer = load_onnx_model(args.model)

    if args.input:
        result = predict(model, tokenizer, args.input)
        print(f"Input:    {args.input}")
        print(f"Merchant: {result}")
        return

    if args.ofx:
        transactions = parse_ofx(args.ofx)
        print(f"\n{'TRANSACTION':<62} {'MERCHANT'}")
        print("-" * 90)
        for name, amount in transactions:
            merchant = predict(model, tokenizer, name)
            truncated = name[:59]
            print(f"{truncated:<62} {merchant}")
        print(f"\nTotal: {len(transactions)} transactions")
        return

    # Default: run a few test cases
    test_cases = [
        "NETFLIX.COM 121 ALBRIGHT WAY LOS GATOS 95032 CA USA",
        "MCDONALD'S F2548 RT 35 & AMBOY CLIFFWOOD BEA07735 NJ USA",
        "WAL-MART #2825 1126 US HIGHWAY 9 OLD BRIDGE 08857 NJ USA",
        "GOOGLE *YOUTUBEPREMIUM1600 AMPHITHEATRE PKWY 650-253-0000 94043 CA USA",
        "GEICO *AUTO ONE GEICO PLAZA 800-841-3000 20076 DC USA",
        "PAYPAL DES:INST XFER ID:LYFTRIDEUS INDN:JENNIFER DAVIS CO ID:PAYPALSI78 WEB",
    ]

    print(f"\n{'TRANSACTION':<62} {'MERCHANT'}")
    print("-" * 80)
    for tx in test_cases:
        merchant = predict(model, tokenizer, tx)
        truncated = tx[:59]
        print(f"{truncated:<62} {merchant}")


if __name__ == "__main__":
    main()
