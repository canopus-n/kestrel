"""
Detect merchant names from transaction descriptions and add as a second column.
"""

import csv
import re
from pathlib import Path

INPUT_FILE = Path(__file__).parent / "transaction_descriptions.csv"
OUTPUT_FILE = INPUT_FILE  # overwrite in place


# US state abbreviations for detecting address boundaries
US_STATES = {
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI",
    "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN",
    "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH",
    "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA",
    "WV", "WI", "WY",
}


def extract_merchant(desc):
    """Extract the merchant name from a transaction description."""

    # --- Payment / internal transfer patterns ---
    if re.match(r"^(AUTOPAY |ACH DEPOSIT|PAYMENT -|AUTOMATIC PAYMENT)", desc, re.IGNORECASE):
        return "PAYMENT"

    # --- Noise / non-transaction lines ---
    if re.match(r"^(PLEASE READ|IMPORTANT CHANGE|SEE REVERSE)", desc, re.IGNORECASE):
        return "NOTICE"

    if re.match(r"^(To Savings|From Savings|Interest earned)", desc, re.IGNORECASE):
        return desc.split(" -")[0].split(",")[0].strip()

    # --- Fidelity brokerage actions ---
    fidelity_match = re.match(
        r"^(REINVESTMENT|DIVIDEND RECEIVED|YOU BOUGHT|YOU SOLD|PARTIC CONTR|"
        r"DEBIT CARD PURCHASE)\s+(.+?)(?:\s*\(Cash\))?$", desc
    )
    if fidelity_match:
        action = fidelity_match.group(1)
        rest = fidelity_match.group(2)
        if action == "DEBIT CARD PURCHASE":
            # "DEBIT CARD PURCHASE FULLSCRIPT* R271829297 US.FULLSCRIPT NH..."
            # "DEBIT CARD PURCHASE CVS/PHARMACY #01088 MATAWAN NJ..."
            # Merchant is the first meaningful word(s) before location/code
            # Strip trailing (Cash) and transaction codes
            rest = re.sub(r"\s+[A-Z]{2}\d{4,}.*$", "", rest)
            # Try to find city+state pattern
            city_state = re.search(r"\s+([A-Z][A-Z]+)\s+([A-Z]{2})$", rest)
            if city_state and city_state.group(2) in US_STATES:
                merchant = rest[:city_state.start()].strip()
            else:
                # Take first few tokens as merchant
                parts = rest.split()
                merchant_parts = []
                for p in parts:
                    if re.match(r"^[A-Z]{2}\d{4,}", p):
                        break
                    if re.match(r"^\d{10,}", p):
                        break
                    if re.match(r"^(HTTPS?|HTTP|WWW\.)", p, re.IGNORECASE):
                        break
                    merchant_parts.append(p)
                    if len(merchant_parts) >= 3:
                        break
                merchant = " ".join(merchant_parts)
            # Clean trailing reference codes and asterisk junk
            merchant = re.sub(r"\s*\*\s*[A-Z0-9]{8,}$", "", merchant)
            merchant = re.sub(r"\s+[A-Z0-9]{10,}$", "", merchant)
            # Clean trailing asterisk
            merchant = merchant.rstrip("* ")
            return merchant.strip() or rest.split()[0]
        else:
            # Fidelity fund actions - extract the fund/stock name
            # "FIDELITY GOVERNMENT CASH RESERVES (FDRXX) (Cash)"
            fund_match = re.match(r"(.+?)\s*\([A-Z]+\)", rest)
            if fund_match:
                return fund_match.group(1).strip()
            return rest.split("(")[0].strip()

    # --- Amazon variants ---
    if re.match(r"^AMAZON\.COM\*", desc):
        return "AMAZON.COM"
    if re.match(r"^AMZN MKTP US", desc):
        return "AMAZON MARKETPLACE"
    if re.match(r"^AMZN\.COM", desc):
        return "AMAZON.COM"
    if re.match(r"^AMZN DIGITAL", desc):
        return "AMAZON DIGITAL"
    if re.match(r"^AMZN INSTALL\*", desc):
        return "AMAZON INSTALLMENTS"
    if re.match(r"^AMAZON MARKETPLACE", desc):
        return "AMAZON MARKETPLACE"
    if re.match(r"^AMAZON RETAIL", desc):
        return "AMAZON RETAIL"
    if re.match(r"^AMAZON DIGITAL", desc):
        return "AMAZON DIGITAL"
    if re.match(r"^PRIME VIDEO", desc):
        return "AMAZON PRIME VIDEO"
    if re.match(r"^MONTHLY INSTALLMENTS", desc):
        return "AMAZON INSTALLMENTS"

    # --- Apple ---
    if re.match(r"^(APL\*|APPLE\.COM)", desc):
        return "APPLE"

    # --- PayPal ---
    paypal_match = re.match(r"^PAYPAL\s+\*?(.+?)(\s+\d|\s+[A-Z]{2}\s+)", desc)
    if paypal_match:
        return "PAYPAL " + paypal_match.group(1).strip()
    if desc.startswith("PAYPAL"):
        # "PAYPAL WALMART COM 4029357733 CA"
        parts = desc.split()
        merchant_parts = []
        for p in parts[1:]:
            if re.match(r"^\d{5,}", p):
                break
            if p in US_STATES and len(p) == 2:
                break
            merchant_parts.append(p)
        return "PAYPAL " + " ".join(merchant_parts) if merchant_parts else "PAYPAL"

    # --- SoFi short descriptions ---
    sofi_known = {
        "ALLY": "ALLY",
        "THE DEPOSITORY T": "THE DEPOSITORY TRUST",
        "DIRECT_DEPOSIT": "DIRECT DEPOSIT",
        "SOFI CHECKING": "SOFI",
    }
    for key, val in sofi_known.items():
        if desc.upper().startswith(key):
            return val

    # --- DD (DoorDash) ---
    # Matches: "DD *KHOKHA 303...", "DD *DOORDASH MCDONALDS303...", "DD DOORDASH DUNKIN 303..."
    if re.match(r"^DD\s", desc):
        # Extract the restaurant name after DD/DOORDASH prefixes
        cleaned = re.sub(r"^DD\s*[/*]*\s*(?:DOORDASH\s+)?(?:STORE)?", "", desc).strip()
        # Take text before the first number sequence (address)
        rest_match = re.match(r"^(.+?)(?:\d{2,})", cleaned)
        if rest_match:
            return "DOORDASH " + rest_match.group(1).strip()
        return "DOORDASH " + cleaned.split()[0] if cleaned else "DOORDASH"

    # --- Google/subscription services ---
    google_match = re.match(r"^GOOGLE\s*\*(.+?)\s", desc)
    if google_match:
        return "GOOGLE " + google_match.group(1).strip()

    # --- OpenAI / ChatGPT ---
    if re.match(r"^(OPENAI|CHATGPT)", desc):
        return "OPENAI"

    # --- TST* (Toast POS) ---
    tst_match = re.match(r"^TST\*\s*(.+?)(?:\d{3,}\s+[A-Z])", desc)
    if tst_match:
        return tst_match.group(1).strip()
    if desc.startswith("TST*"):
        parts = desc[4:].strip().split()
        merchant_parts = []
        for p in parts:
            if re.match(r"^\d{3,}", p):
                break
            merchant_parts.append(p)
            if len(merchant_parts) >= 4:
                break
        return " ".join(merchant_parts) if merchant_parts else desc[4:].split()[0]

    # --- Uber ---
    if re.match(r"^UBER\s*\*?\s*(EATS|TRIP|RIDE)?", desc):
        uber_match = re.match(r"^UBER\s*\*?\s*(EATS|TRIP|RIDE)?", desc)
        suffix = uber_match.group(1) if uber_match.group(1) else ""
        return ("UBER " + suffix).strip()

    # --- Square (SQ *) ---
    sq_match = re.match(r"^SQ\s*\*\s*(.+?)(?:\s+\d|\s+[A-Z]{2}\s*$)", desc)
    if sq_match:
        return sq_match.group(1).strip()

    # --- Standard OFX/Apple Card format: MERCHANT <address> <zip> <state> USA ---
    # Try to find the address boundary using common patterns:
    # 1. Street number followed by street name
    # 2. Zip code pattern (5 digits or 5-4)
    # 3. State abbreviation + USA at end

    # Pattern: MERCHANT_NAME <number> <street> <city> <zip> <state> <country>
    addr_match = re.match(
        r"^(.+?)\s+\d+\s+(?:[A-Z0-9].*?\s+)"
        r"(?:[A-Z]+\s+)?\d{5}(?:-\d{4})?\s*[A-Z]{2}\s+(?:USA|US)\s*$",
        desc
    )
    if addr_match:
        merchant = addr_match.group(1).strip()
        # Remove trailing store numbers like #0222 or *code
        return merchant

    # Simpler pattern: look for 5-digit zip near end
    zip_match = re.search(r"\s(\d{5}(?:-?\d{4})?)\s*([A-Z]{2})?\s*(USA|US|HKG|NLD|GBR|CAN)?\s*$", desc)
    if zip_match:
        # Everything before the zip's preceding city/address is likely the merchant
        before_zip = desc[:zip_match.start()]
        # Find where the address starts (first digit sequence that looks like a street number)
        street_match = re.search(r"\s\d{1,5}\s+[A-Z]", before_zip)
        if street_match:
            merchant = before_zip[:street_match.start()].strip()
            if merchant:
                return merchant

    # Pattern for descriptions ending with state abbreviation (no zip visible)
    # e.g. "COSTCO GAS #0222 HAZLET NJ"
    state_end_match = re.match(
        r"^(.+?)\s+([A-Z][a-z]+|[A-Z]+)\s+([A-Z]{2})\s*$", desc
    )
    if state_end_match and state_end_match.group(3) in US_STATES:
        candidate = state_end_match.group(1).strip()
        # The candidate might still include a street address
        # Check if it ends with a number (likely part of address)
        if not re.search(r"\d$", candidate):
            return candidate

    # --- Chase format: "MERCHANT CITY STATE" ---
    # e.g. "COSTCO GAS #0222 HAZLET NJ"
    chase_match = re.match(r"^(.+?)\s{2,}", desc)
    if chase_match:
        return chase_match.group(1).strip()

    # --- Product descriptions from Amazon PDFs (no address, mixed case) ---
    if re.match(r"^[A-Z][a-z]", desc) or re.match(r"^[a-z]", desc):
        # These are product names — merchant is Amazon
        return "AMAZON"

    # --- Descriptions that are just short merchant names (SoFi, etc.) ---
    if len(desc.split()) <= 3 and not re.search(r"\d{5}", desc):
        return desc.strip()

    # --- Fallback: take everything before the first number sequence that looks like an address ---
    fallback_match = re.match(r"^([A-Z][A-Z\s&.*#/\'-]+?)(?:\s+\d{1,5}\s+[A-Z])", desc)
    if fallback_match:
        return fallback_match.group(1).strip()

    # Last resort: return first 2-3 meaningful words
    words = desc.split()
    if len(words) >= 2:
        # Take words until we hit a number or known address token
        merchant_words = []
        for w in words:
            if re.match(r"^\d+$", w) and len(merchant_words) >= 1:
                break
            merchant_words.append(w)
            if len(merchant_words) >= 3:
                break
        return " ".join(merchant_words)

    return desc


def main():
    # Read existing descriptions
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Extract merchants
    results = []
    for row in rows:
        desc = row["description"]
        merchant = extract_merchant(desc)
        # Clean up merchant name
        merchant = re.sub(r"\s+", " ", merchant).strip()
        merchant = re.sub(r"[#*]+$", "", merchant).strip()
        # Remove internal asterisks used as separators (e.g. "GEICO *AUTO" -> "GEICO AUTO")
        merchant = re.sub(r"\s*\*\s*", " ", merchant).strip()
        merchant = re.sub(r"\s*\(RETURN\)$", "", merchant)
        # Remove store numbers like #01088, #0222
        merchant = re.sub(r"\s*#\d+\s*$", "", merchant).strip()
        # Remove trailing city names (single word all caps that's a known city pattern)
        merchant = re.sub(r"\s+[A-Z]{2,}$", "", merchant).strip() if re.search(r"\s[A-Z]{2,}$", merchant) and len(merchant.split()) > 2 else merchant
        # Remove store location codes like "S1", "062300071"
        merchant = re.sub(r"\s+S\d+$", "", merchant).strip()
        merchant = re.sub(r"\s+\d{5,}$", "", merchant).strip()
        # Remove trailing dash or hyphen
        merchant = merchant.rstrip(" -")
        # Remove trailing ampersand or HTML entities
        merchant = re.sub(r"\s*&amp;?\s*$", "", merchant).strip()
        merchant = re.sub(r"\s*&\s*$", "", merchant).strip()
        # Normalize DD DOORDASH prefix
        merchant = re.sub(r"^DD\s+DOORDASH\s+", "DOORDASH ", merchant).strip()
        merchant = re.sub(r"^DD\s+", "DOORDASH ", merchant).strip()
        # Remove trailing "SUBS" fragments (from truncated descriptions)
        merchant = re.sub(r"\s+SUBS\w*$", "", merchant).strip()
        # Remove trailing city/location names from known chain merchants
        chain_patterns = [
            (r"^(SHOPRITE)\s+\w+", r"\1"),
            (r"^(COSTCO)\s+GAS", r"\1 GAS"),
            (r"^(QUICK CHEK)\s+CORP", r"\1"),
            (r"^(WAWA)\s+\d+", r"\1"),
            (r"^(DUNKIN)\s+#?\d+", r"\1"),
            (r"^(CVS/PHARMACY)\s*", r"CVS"),
            (r"^(CVS)\s+CAREPASS", r"CVS"),
            (r"^(DOLLAR GENERAL)\s+#?\d+", r"\1"),
            (r"^(DOLLARTREE)\s+\d+", r"DOLLAR TREE"),
            (r"^(MARSHALLS)\s+#?\d+", r"\1"),
            (r"^(WAL-MART)\s+#?\d+", r"WALMART"),
            (r"^(WAL-MART)", r"WALMART"),
            (r"^(TARGET)\s+\d+", r"\1"),
            (r"^(PEPBOYS STORE)\s+\d+", r"PEP BOYS"),
            (r"^(THE HOME DEPOT)\s+#?\d+", r"THE HOME DEPOT"),
            (r"^(THE HOME)\s*$", r"THE HOME DEPOT"),
            (r"^(GEICO)\s+AUTO", r"GEICO"),
            (r"^(NETFLIX),?\s+INC\.?", r"NETFLIX"),
            (r"^(EXXON)\s+\w+\s+GAS", r"EXXON"),
            (r"^(STARBUCKS)\s+\d+", r"STARBUCKS"),
        ]
        for pattern, replacement in chain_patterns:
            if re.match(pattern, merchant, re.IGNORECASE):
                merchant = re.sub(pattern, replacement, merchant, flags=re.IGNORECASE)
                break
        results.append({"description": desc, "merchant": merchant})

    # Write back
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["description", "merchant"])
        writer.writeheader()
        writer.writerows(results)

    print(f"Added merchant column to {len(results)} rows.")
    print(f"Output: {OUTPUT_FILE}")

    # Show some samples
    print("\nSamples:")
    import random
    random.seed(42)
    samples = random.sample(results, min(20, len(results)))
    for s in samples:
        print(f"  {s['description'][:60]:<60} -> {s['merchant']}")


if __name__ == "__main__":
    main()
