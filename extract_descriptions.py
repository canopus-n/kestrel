"""
Extract unique transaction descriptions from all files in the Data/ directory.
Supports: .ofx, .qfx (OFX/QFX format), .csv (multiple formats), .pdf (Amazon/Synchrony statements)
"""

import csv
import re
import os
from pathlib import Path

import pdfplumber

DATA_DIR = Path(__file__).parent / "Data"
OUTPUT_FILE = Path(__file__).parent / "transaction_descriptions.csv"


def extract_from_ofx_qfx(filepath):
    """Extract <NAME> tags from OFX/QFX files."""
    descriptions = []
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    matches = re.findall(r"<NAME>([^<]+)", content)
    for m in matches:
        desc = m.strip()
        if desc:
            descriptions.append(desc)
    return descriptions


def extract_from_pdf(filepath):
    """Extract transaction descriptions from Amazon/Synchrony PDF statements."""
    descriptions = []
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
            # Look for transaction lines: date pattern followed by reference and description
            # Format: MM/DD <reference> <DESCRIPTION> <optional city state> $amount
            # We extract the description part (merchant + product lines)
            lines = text.split("\n")
            in_transactions = False
            for line in lines:
                stripped = line.strip()
                # Detect start of transaction section
                if "Transaction Detail" in stripped:
                    in_transactions = True
                    continue
                if not in_transactions:
                    continue
                # Skip header lines
                if stripped.startswith("Date") and "Reference" in stripped:
                    continue
                # Skip section headers like "Payments", "Other Credits", "Purchases and Other Debits"
                if re.match(r"^(Payments|Other Credits|Purchases and Other Debits)", stripped):
                    continue
                # Match transaction lines: MM/DD <ref> <description> <amount>
                # e.g. "06/13 F9342005400CHGDDA AUTOMATIC PAYMENT - THANK YOU -$563.57"
                # e.g. "05/20 P9342004FEHMBN91P AMAZON MARKETPLACE SEATTLE WA $46.99"
                txn_match = re.match(
                    r"^\d{2}/\d{2}\s+\S+\s+(.+?)\s+[-]?\$[\d,]+\.\d{2}$", stripped
                )
                if txn_match:
                    desc = txn_match.group(1).strip()
                    if desc:
                        descriptions.append(desc)
                    continue
                # Also capture continuation/product description lines that aren't
                # reference numbers or amounts (multi-line descriptions)
                # These are lines that don't start with a date and aren't just codes
                if (
                    not re.match(r"^\d{2}/\d{2}\s", stripped)
                    and not re.match(r"^[-]?\$", stripped)
                    and not re.match(r"^[A-Z][a-z]", stripped)  # skip "Page X of Y" etc
                    and stripped
                    and not stripped.startswith("PAGE")
                    and "Visit us at" not in stripped
                    and "Account Number" not in stripped
                    and "Cardholder" not in stripped
                ):
                    # Skip pure alphanumeric codes (order IDs like "BRerNxzxOCAX")
                    if not re.match(r"^[A-Za-z0-9]{10,}$", stripped):
                        # Skip boilerplate/noise lines
                        noise_patterns = [
                            r"^\(Continued",
                            r"^Transaction Detail",
                            r"^\d{4} Year-to-Date",
                            r"^Total (Fees|Interest)",
                            r"^Type of\s",
                            r"^Expiration",
                            r"^Annual",
                            r"^Balance Subject",
                            r"^Interest\s+Charge",
                            r"^Purchases.*N/A",
                            r"^\(including",
                            r"^NOTICE:",
                            r"^Manage your account",
                            r"^Here's one more",
                            r"^Amazon Pay",
                            r"^select your",
                            r"^If you have promotional",
                            r"^\* Expired",
                            r"^expiration\.",
                        ]
                        if any(re.match(p, stripped) for p in noise_patterns):
                            continue
                        # This is likely a product description line
                        if len(stripped) > 5:
                            descriptions.append(stripped)
    return descriptions


def extract_from_csv_chase(filepath):
    """Extract 'Payee' column from Chase-style CSVs (Posted Date,Reference Number,Payee,Address,Amount)."""
    descriptions = []
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        # Skip blank lines before header
        lines = f.readlines()
    header_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("Posted Date,"):
            header_idx = i
            break
    if header_idx is None:
        return descriptions
    reader = csv.DictReader(lines[header_idx:])
    for row in reader:
        if "Payee" in row and row["Payee"]:
            descriptions.append(row["Payee"].strip())
    return descriptions


def extract_from_csv_sofi(filepath):
    """Extract 'Description' column from SoFi-style CSVs (Date,Description,Type,Amount,...)."""
    descriptions = []
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    header_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("Date,Description,"):
            header_idx = i
            break
    if header_idx is None:
        return descriptions
    reader = csv.DictReader(lines[header_idx:])
    for row in reader:
        if "Description" in row and row["Description"]:
            descriptions.append(row["Description"].strip())
    return descriptions


def extract_from_csv_fidelity(filepath):
    """Extract 'Action' column from Fidelity-style CSVs (Run Date,Action,Symbol,Description,...)."""
    descriptions = []
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    header_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("Run Date,"):
            header_idx = i
            break
    if header_idx is None:
        return descriptions
    reader = csv.DictReader(lines[header_idx:])
    for row in reader:
        if "Action" in row and row["Action"]:
            descriptions.append(row["Action"].strip())
    return descriptions


def detect_csv_type(filepath):
    """Detect which CSV format a file uses based on its header."""
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("Posted Date,"):
            return "chase"
        elif stripped.startswith("Date,Description,"):
            return "sofi"
        elif stripped.startswith("Run Date,"):
            return "fidelity"
        else:
            break
    return None


def main():
    all_descriptions = set()
    file_count = 0

    for filepath in sorted(DATA_DIR.iterdir()):
        if filepath.is_dir():
            continue

        ext = filepath.suffix.lower()

        if ext in (".ofx", ".qfx"):
            descs = extract_from_ofx_qfx(filepath)
            all_descriptions.update(descs)
            file_count += 1
            print(f"  [OFX/QFX] {filepath.name}: {len(descs)} descriptions")

        elif ext == ".csv":
            csv_type = detect_csv_type(filepath)
            if csv_type == "chase":
                descs = extract_from_csv_chase(filepath)
            elif csv_type == "sofi":
                descs = extract_from_csv_sofi(filepath)
            elif csv_type == "fidelity":
                descs = extract_from_csv_fidelity(filepath)
            else:
                # Try all parsers as fallback
                descs = extract_from_csv_chase(filepath)
                if not descs:
                    descs = extract_from_csv_sofi(filepath)
                if not descs:
                    descs = extract_from_csv_fidelity(filepath)
                if not descs:
                    print(f"  [CSV] WARNING: Could not parse {filepath.name}")
                    continue
            all_descriptions.update(descs)
            file_count += 1
            print(f"  [CSV/{csv_type}] {filepath.name}: {len(descs)} descriptions")

        elif ext == ".pdf":
            descs = extract_from_pdf(filepath)
            all_descriptions.update(descs)
            file_count += 1
            print(f"  [PDF] {filepath.name}: {len(descs)} descriptions")

        else:
            print(f"  [SKIP] Unsupported file type: {filepath.name}")
            continue

    # Write deduplicated descriptions to CSV
    sorted_descriptions = sorted(all_descriptions)
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["description"])
        for desc in sorted_descriptions:
            writer.writerow([desc])

    print(f"\nProcessed {file_count} files.")
    print(f"Extracted {len(sorted_descriptions)} unique transaction descriptions.")
    print(f"Output written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
