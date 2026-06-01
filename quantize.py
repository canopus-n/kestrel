"""
Quantize the Kestrel ONNX model to INT8 for smaller size and faster inference.

Reduces model size from ~593MB to ~150MB with negligible accuracy loss.
"""

from pathlib import Path
from onnxruntime.quantization import quantize_dynamic, QuantType


def quantize_model(input_path: Path, output_path: Path):
    """Quantize a single ONNX model to INT8."""
    print(f"  Quantizing {input_path.name}...")
    input_size = input_path.stat().st_size / 1024 / 1024

    quantize_dynamic(
        model_input=str(input_path),
        model_output=str(output_path),
        weight_type=QuantType.QInt8,
    )

    output_size = output_path.stat().st_size / 1024 / 1024
    ratio = output_size / input_size * 100
    print(f"    {input_size:.1f} MB -> {output_size:.1f} MB ({ratio:.0f}%)")


def main():
    onnx_dir = Path("./output/onnx")
    quant_dir = Path("./output/onnx-quantized")
    quant_dir.mkdir(parents=True, exist_ok=True)

    if not onnx_dir.exists():
        print("Error: ONNX models not found at ./output/onnx")
        print("Run export_onnx.py first.")
        return

    # Models to quantize
    model_files = [
        "encoder_model.onnx",
        "decoder_model.onnx",
        "decoder_with_past_model.onnx",
    ]

    print("Quantizing models to INT8...\n")
    total_input = 0
    total_output = 0

    for model_file in model_files:
        input_path = onnx_dir / model_file
        output_path = quant_dir / model_file

        if not input_path.exists():
            print(f"  Skipping {model_file} (not found)")
            continue

        total_input += input_path.stat().st_size
        quantize_model(input_path, output_path)
        total_output += output_path.stat().st_size

    # Copy non-model files (config, tokenizer, etc.)
    print("\nCopying config and tokenizer files...")
    import shutil
    for f in onnx_dir.iterdir():
        if f.suffix != ".onnx" and f.name != ".DS_Store":
            dest = quant_dir / f.name
            shutil.copy2(f, dest)
            print(f"  {f.name}")

    print(f"\n{'='*50}")
    print(f"Total: {total_input/1024/1024:.1f} MB -> {total_output/1024/1024:.1f} MB")
    print(f"Reduction: {(1 - total_output/total_input)*100:.0f}%")
    print(f"\nQuantized models saved to: {quant_dir}")
    print("\nNext: test with 'python test.py --model output/onnx-quantized'")


if __name__ == "__main__":
    main()
