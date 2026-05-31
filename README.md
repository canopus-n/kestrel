# Kestrel

Merchant name extraction model for credit card transaction strings.

Fine-tuned DistilBERT that takes raw transaction descriptions like:
```
MCDONALD'S F2548 RT 35 & AMBOY CLIFFWOOD BEA07735 NJ USA
PAYPAL DES:INST XFER ID:LYFTRIDEUS INDN:JENNIFER DAVIS CO ID:PAYPALSI78 WEB
TRADER_JS_092 07/08 #XXXXX0092 PURCHASE GROCERIES MONROVIA CA
```

And extracts clean merchant names:
```
McDonald's
Lyft
Trader Joe's
```

## Training Data

- [crossingminds/credit_card_3k](https://huggingface.co/datasets/crossingminds/credit_card_3k) — 3,111 real credit card transaction → merchant pairs
- Custom data (Apple Card, Chase, Capital One formats)

## Usage

```bash
# Setup
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Train
python train.py

# Export to ONNX
python export_onnx.py

# Test
python test.py --input "NETFLIX.COM 121 ALBRIGHT WAY LOS GATOS 95032 CA USA"
```

## Architecture

- Base model: `distilbert-base-uncased`
- Task: Sequence-to-sequence (input: transaction string, output: merchant name)
- Training: ~3K examples, 5 epochs, ~15 min on Apple Silicon
- Output: ONNX model (~65MB) for use in Puffin's import pipeline
