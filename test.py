"""
Test the trained Kestrel model on custom inputs or the Apple Card OFX file.

Usage:
    python test.py --input "MCDONALD'S F2548 RT 35 & AMBOY CLIFFWOOD BEA07735 NJ USA"
    python test.py --ofx "/path/to/file.ofx"
    python test.py  # runs default test cases
"""

import argparse
import re
from pathlib import Path

import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer


def load_model(model_path="./output/final"):
    """Load the trained model and tokenizer."""
    path = Path(model_path)
    if not path.exists():
        print(f"Error: Model not found at {path}")
        print("Run train.py first.")
        exit(1)

    tokenizer = T5Tokenizer.from_pretrained(path)
    model = T5ForConditionalGeneration.from_pretrained(path)
    model.eval()

    if torch.backends.mps.is_available():
        model = model.to("mps")
    elif torch.cuda.is_available():
        model = model.to("cuda")

    return model, tokenizer


def predict(model, tokenizer, transaction: str) -> str:
    """Extract merchant name from a transaction string."""
    input_text = f"extract merchant: {transaction}"
    inputs = tokenizer(input_text, return_tensors="pt", max_length=128, truncation=True)

    device = next(model.parameters()).device
    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
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
    parser = argparse.ArgumentParser(description="Test Kestrel merchant extraction")
    parser.add_argument("--input", "-i", type=str, help="Single transaction string to test")
    parser.add_argument("--ofx", type=str, help="Path to OFX file to test")
    parser.add_argument("--model", type=str, default="./output/final", help="Model path")
    args = parser.parse_args()

    model, tokenizer = load_model(args.model)

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

    # Default test cases
    test_cases = [
        ("NETFLIX.COM 121 ALBRIGHT WAY LOS GATOS 95032 CA USA", "Netflix"),
        ("MCDONALD'S F2548 RT 35 & AMBOY CLIFFWOOD BEA07735 NJ USA", "McDonald's"),
        ("WAL-MART #2825 1126 US HIGHWAY 9 OLD BRIDGE 08857 NJ USA", "Walmart"),
        ("GOOGLE *YOUTUBEPREMIUM1600 AMPHITHEATRE PKWY 650-253-0000 94043 CA USA", "YouTube Premium"),
        ("PAYPAL DES:INST XFER ID:LYFTRIDEUS INDN:JENNIFER DAVIS CO ID:PAYPALSI78 WEB", "Lyft"),
        ("TRADER_JS_092 07/08 #XXXXX0092 PURCHASE GROCERIES MONROVIA CA", "Trader Joe's"),
        ("GEICO *AUTO ONE GEICO PLAZA 800-841-3000 20076 DC USA", "GEICO"),
        ("APPLE.COM/BILL ONE APPLE PARK WAY 866-712-7753 95014 CA USA", "Apple"),
        ("SHOPRITE HAZLET S1 3150 STATE HIGHWAY 35 HAZLET 07735 NJ USA", "ShopRite"),
        ("NJ EZPASS 375 MCCARTER HIGHWAY NEWARK 07114 NJ USA", "NJ E-ZPass"),
        ("ACH DEPOSIT INTERNET TRANSFER FROM ACCOUNT ENDING IN 1986", ""),
        ("DAILY CASH ADJUSTMENT", ""),
    ]

    print(f"\n{'TRANSACTION':<62} {'PREDICTED':<20} {'EXPECTED'}")
    print("-" * 100)

    correct = 0
    for tx, expected in test_cases:
        predicted = predict(model, tokenizer, tx)
        match = "✓" if predicted.lower() == expected.lower() else "✗"
        truncated = tx[:59]
        print(f"{match} {truncated:<60} {predicted:<20} {expected}")
        if predicted.lower() == expected.lower():
            correct += 1

    print(f"\nAccuracy: {correct}/{len(test_cases)} ({100*correct/len(test_cases):.0f}%)")


if __name__ == "__main__":
    main()
