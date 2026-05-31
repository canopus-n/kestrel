"""
Export the trained Kestrel model to ONNX format for use in Puffin.

Uses HuggingFace Optimum for clean ONNX export with proper input/output naming.
"""

from pathlib import Path
from optimum.onnxruntime import ORTModelForSeq2SeqLM
from transformers import T5Tokenizer


def main():
    model_path = Path("./output/final")
    onnx_path = Path("./output/onnx")

    if not model_path.exists():
        print(f"Error: Model not found at {model_path}")
        print("Run train.py first.")
        return

    print(f"Loading model from {model_path}...")
    tokenizer = T5Tokenizer.from_pretrained(model_path)

    # Export to ONNX using Optimum
    print(f"Exporting to ONNX at {onnx_path}...")
    model = ORTModelForSeq2SeqLM.from_pretrained(model_path, export=True)
    model.save_pretrained(onnx_path)
    tokenizer.save_pretrained(onnx_path)

    # Print file sizes
    print("\nExported files:")
    total_size = 0
    for f in sorted(onnx_path.rglob("*.onnx")):
        size = f.stat().st_size
        total_size += size
        print(f"  {f.name}: {size / 1024 / 1024:.1f} MB")

    print(f"\n  Total ONNX size: {total_size / 1024 / 1024:.1f} MB")

    # Quick sanity check
    print("\nRunning sanity check...")
    from optimum.onnxruntime import ORTModelForSeq2SeqLM as ORT

    ort_model = ORT.from_pretrained(onnx_path)
    test_input = "extract merchant: NETFLIX.COM 121 ALBRIGHT WAY LOS GATOS 95032 CA USA"
    inputs = tokenizer(test_input, return_tensors="pt")
    outputs = ort_model.generate(**inputs, max_length=64)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"  Input:  NETFLIX.COM 121 ALBRIGHT WAY LOS GATOS 95032 CA USA")
    print(f"  Output: {result}")

    print(f"\nDone! ONNX model ready at {onnx_path}")


if __name__ == "__main__":
    main()
