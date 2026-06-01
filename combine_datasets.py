"""
Combine transaction descriptions from:
1. transaction_descriptions.csv (local extracted data)
2. crossingminds/credit_card_3k (HuggingFace dataset, train + test splits)

Output: combined_transactions.csv with columns [description, merchant]
Deduplicated on the description column.
"""

import csv
from pathlib import Path
from datasets import load_dataset

OUTPUT_FILE = Path(__file__).parent / "combined_transactions.csv"
LOCAL_FILE = Path(__file__).parent / "transaction_descriptions.csv"


def main():
    combined = {}  # description -> merchant (dict for dedup)

    # 1. Load local transaction_descriptions.csv
    print("Loading local transaction_descriptions.csv...")
    with open(LOCAL_FILE, "r", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        for row in reader:
            desc = row["description"].strip()
            merchant = row["merchant"].strip()
            if desc and desc not in combined:
                combined[desc] = merchant
    local_count = len(combined)
    print(f"  Loaded {local_count} descriptions from local file.")

    # 2. Load crossingminds/credit_card_3k (train + test)
    print("Loading crossingminds/credit_card_3k from HuggingFace...")
    for split in ["train", "test"]:
        ds = load_dataset("crossingminds/credit_card_3k", split=split)
        for row in ds:
            desc = row["string"].strip()
            merchant = row["merchant"].strip()
            if desc and desc not in combined:
                combined[desc] = merchant
    hf_count = len(combined) - local_count
    print(f"  Loaded {hf_count} new descriptions from HuggingFace (after dedup).")

    # 3. Write combined output
    print(f"\nWriting combined dataset...")
    sorted_items = sorted(combined.items(), key=lambda x: x[0])
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["description", "merchant"])
        for desc, merchant in sorted_items:
            writer.writerow([desc, merchant])

    print(f"Total unique descriptions: {len(sorted_items)}")
    print(f"  - From local data: {local_count}")
    print(f"  - From crossingminds/credit_card_3k: {hf_count}")
    print(f"Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
