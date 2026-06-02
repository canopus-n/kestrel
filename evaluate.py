"""
Evaluate Kestrel on held-out eval sets with proper metrics.

Usage:
  python evaluate.py
  python evaluate.py --model output/final --onnx output/onnx
  python evaluate.py --failures 20
  python evaluate.py --json eval_report.json
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import torch
from transformers import AutoTokenizer, T5ForConditionalGeneration

from kestrel_metrics import (
    empty_metrics,
    exact_match,
    is_no_merchant,
    load_aliases,
    merchant_metrics,
    normalize_prediction,
    normalized_match,
    token_f1,
)

ROOT = Path(__file__).parent
PREFIX = "extract merchant: "


def load_model(model_path: Path):
    tokenizer = AutoTokenizer.from_pretrained("t5-small")
    model = T5ForConditionalGeneration.from_pretrained(model_path)
    model.eval()
    if torch.backends.mps.is_available():
        model = model.to("mps")
    elif torch.cuda.is_available():
        model = model.to("cuda")
    return model, tokenizer


def load_onnx_model(model_path: Path):
    from optimum.onnxruntime import ORTModelForSeq2SeqLM

    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = ORTModelForSeq2SeqLM.from_pretrained(model_path)
    return model, tokenizer


def predict(model, tokenizer, description: str) -> str:
    input_text = PREFIX + description
    inputs = tokenizer(input_text, return_tensors="pt", max_length=128, truncation=True)
    device = next(model.parameters()).device if hasattr(model, "parameters") else None
    if device is not None:
        inputs = {k: v.to(device) for k, v in inputs.items()}
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=64)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


def load_csv_eval(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_manual_eval(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data


def run_eval_set(
    name: str,
    rows: list[dict],
    model,
    tokenizer,
    aliases: dict[str, str],
    failure_limit: int,
) -> dict:
    descriptions = [r["description"] for r in rows]
    expected = [r["merchant"] for r in rows]
    predictions = [predict(model, tokenizer, d) for d in descriptions]

    merchant_rows = [(p, e, d) for p, e, d in zip(predictions, expected, descriptions, strict=True) if not is_no_merchant(e)]
    non_merchant_rows = [(p, e, d) for p, e, d in zip(predictions, expected, descriptions, strict=True) if is_no_merchant(e)]

    m_preds, m_exp, _ = zip(*[(p, e, d) for p, e, d in merchant_rows]) if merchant_rows else ([], [], [])
    nm_preds, nm_exp, _ = zip(*[(p, e, d) for p, e, d in non_merchant_rows]) if non_merchant_rows else ([], [], [])

    result = {
        "name": name,
        "total": len(rows),
        "merchant": merchant_metrics(list(m_preds), list(m_exp), aliases),
        "non_merchant": empty_metrics(list(nm_preds), list(nm_exp)) if nm_preds else {"count": 0},
    }
    if nm_preds:
        result["non_merchant"]["count"] = len(nm_preds)

    failures = []
    for pred, exp, desc in zip(predictions, expected, descriptions, strict=True):
        if not normalized_match(pred, exp, aliases):
            failures.append(
                {
                    "description": desc,
                    "expected": exp if not is_no_merchant(exp) else "(empty)",
                    "predicted": normalize_prediction(pred) or "(empty)",
                    "exact": exact_match(pred, exp, aliases),
                    "token_f1": round(token_f1(pred, exp), 3),
                }
            )
    failures.sort(key=lambda x: x["token_f1"])
    result["failure_count"] = len(failures)
    result["failures"] = failures[:failure_limit]
    return result


def print_report(report: dict) -> None:
    print(f"\n{'=' * 60}")
    print(f"Model: {report['model_path']}")
    print(f"{'=' * 60}")

    for block in report["sets"]:
        print(f"\n--- {block['name']} ({block['total']} rows) ---")
        m = block["merchant"]
        if m["count"]:
            print(
                f"  Merchant: exact={m['exact_match_rate']:.1%}  "
                f"normalized={m['normalized_match_rate']:.1%}  "
                f"token_f1={m['mean_token_f1']:.3f}  (n={m['count']})"
            )
        nm = block["non_merchant"]
        if nm.get("count", 0):
            print(
                f"  Non-merchant: empty_precision={nm['empty_precision']:.1%}  "
                f"empty_recall={nm['empty_recall']:.1%}  "
                f"empty_f1={nm['empty_f1']:.3f}  "
                f"false_merchants={nm['false_merchant_count']}  "
                f"missed_empty={nm['missed_empty_count']}  (n={nm['count']})"
            )
        print(f"  Normalized failures: {block['failure_count']}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", type=str, default="./output/final")
    parser.add_argument("--onnx", type=str, help="Also evaluate ONNX model at this path")
    parser.add_argument("--failures", type=int, default=10, help="Max failures per set to include")
    parser.add_argument("--json", type=str, help="Write full report JSON to this path")
    parser.add_argument(
        "--export-failures",
        action="store_true",
        help="Also write eval_failures.csv (run export_eval_failures.py)",
    )
    args = parser.parse_args()

    model_path = Path(args.model)
    if not model_path.exists():
        raise SystemExit(f"Model not found: {model_path}. Run train.py first.")

    aliases = load_aliases()
    eval_sets = []
    for path, loader in [
        (ROOT / "eval_manual.json", load_manual_eval),
        (ROOT / "eval_merchant.csv", load_csv_eval),
        (ROOT / "eval_non_merchant.csv", load_csv_eval),
    ]:
        if not path.exists():
            raise SystemExit(f"Missing {path}. Run: python create_eval_sets.py")
        eval_sets.append((path.stem, loader(path)))

    # PyTorch eval
    print(f"Loading PyTorch model from {model_path}...")
    model, tokenizer = load_model(model_path)
    report = {"model_path": str(model_path), "sets": []}
    for name, rows in eval_sets:
        report["sets"].append(run_eval_set(name, rows, model, tokenizer, aliases, args.failures))
    print_report(report)

    if args.onnx:
        onnx_path = Path(args.onnx)
        print(f"\nLoading ONNX model from {onnx_path}...")
        onnx_model, onnx_tok = load_onnx_model(onnx_path)
        onnx_report = {"model_path": str(onnx_path), "sets": []}
        for name, rows in eval_sets:
            onnx_report["sets"].append(
                run_eval_set(name, rows, onnx_model, onnx_tok, aliases, args.failures)
            )
        print_report(onnx_report)
        if args.json:
            out = {"pytorch": report, "onnx": onnx_report}
            Path(args.json).write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
            print(f"\nWrote {args.json}")
    elif args.json:
        Path(args.json).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(f"\nWrote {args.json}")

    if args.export_failures:
        import subprocess
        import sys

        subprocess.call([sys.executable, str(ROOT / "export_eval_failures.py")])


if __name__ == "__main__":
    main()