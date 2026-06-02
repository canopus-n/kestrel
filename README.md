# Kestrel

Merchant name extraction model for credit card transaction strings.

Fine-tuned T5-small that takes raw transaction descriptions like:
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

- [crossingminds/credit_card_3k](https://huggingface.co/datasets/crossingminds/credit_card_3k) — 3,111 real and synthetic credit card transaction → merchant pairs
- Additional real and synthetic transactions extracted from OFX, QFX, CSV, and PDF statements (~1,200 unique descriptions)
- Targeted training examples for edge cases (205 examples)
- **Total: ~5,500 training examples**

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

- Base model: `t5-small`
- Task: Sequence-to-sequence (input: transaction string, output: merchant name)
- Training: ~5.5K examples, 10 epochs
- Output: ONNX model (~96MB quantized) for use in transaction enrichment pipelines

### Estimated Training Time

| Hardware | Est. Time (10 epochs) |
|----------|----------------------|
| Apple M1 Max (MPS) | ~23 min |
| Apple M2 Ultra (MPS) | ~13 min |
| Apple M4 Pro (MPS) | ~17 min |
| NVIDIA RTX 3090 | ~6 min |
| NVIDIA RTX 4090 | ~4 min |
| NVIDIA A100 40GB | ~3 min |
| NVIDIA H100 | ~2 min |
| Intel CPU (8-core) | ~73 min |

**Cloud GPU services:**

| Service | GPU | Est. Time |
|---------|-----|-----------|
| Google Colab (free) | T4 | ~15 min |
| GCP (g2-standard) | L4 | ~8 min |
| AWS (g5.xlarge) | A10G | ~7 min |
| AWS (p4d.24xlarge) | A100 | ~3 min |
| Lambda / RunPod | H100 | ~2 min |
