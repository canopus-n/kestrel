"""
Shared normalization and evaluation metrics for Kestrel.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

NO_MERCHANT = " "


def norm_key(text: str) -> str:
    s = text.lower().strip()
    return re.sub(r"[^a-z0-9]+", "", s)


def is_no_merchant(label: str) -> bool:
    return not label or not label.strip() or label == NO_MERCHANT


def normalize_prediction(pred: str) -> str:
    pred = pred.strip()
    if is_no_merchant(pred):
        return ""
    return pred


def load_aliases(path: Path | None = None) -> dict[str, str]:
    path = path or Path(__file__).parent / "merchant_aliases.csv"
    if not path.exists():
        return {}
    mapping: dict[str, str] = {}
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            alias = row.get("alias", "").strip()
            canonical = row.get("canonical", "").strip()
            if alias and canonical:
                mapping[alias] = canonical
    return mapping


def canonicalize(name: str, aliases: dict[str, str]) -> str:
    if is_no_merchant(name):
        return ""
    return aliases.get(name, name).strip()


def exact_match(pred: str, expected: str, aliases: dict[str, str] | None = None) -> bool:
    aliases = aliases or {}
    p = canonicalize(normalize_prediction(pred), aliases)
    e = canonicalize(expected, aliases)
    return p.lower() == e.lower()


def _token_set(name: str) -> set[str]:
    return {norm_key(part) for part in re.split(r"[\s&]+", name) if norm_key(part)}


def token_subset_match(pred: str, expected: str, aliases: dict[str, str] | None = None) -> bool:
    """
    True when one label is a reasonable subset of the other (e.g. expected LOVELY,
    predicted LOVELY & KANDAHAR, or expected ALTICEMOBILE.COM vs predicted ALTICEMOBILE).
    """
    aliases = aliases or {}
    p = canonicalize(normalize_prediction(pred), aliases)
    e = canonicalize(expected, aliases)
    if is_no_merchant(e) or is_no_merchant(p):
        return False
    if norm_key(p) == norm_key(e):
        return True
    pt, et = _token_set(p), _token_set(e)
    if et and pt and (et <= pt or pt <= et):
        return True
    pk, ek = norm_key(p), norm_key(e)
    return bool(pk and ek and (pk in ek or ek in pk))


def normalized_match(pred: str, expected: str, aliases: dict[str, str] | None = None) -> bool:
    aliases = aliases or {}
    p = canonicalize(normalize_prediction(pred), aliases)
    e = canonicalize(expected, aliases)
    if is_no_merchant(e) and is_no_merchant(p):
        return True
    if is_no_merchant(e) != is_no_merchant(p):
        return False
    if norm_key(p) == norm_key(e):
        return True
    return token_subset_match(pred, expected, aliases)


def token_f1(pred: str, expected: str) -> float:
    p = canonicalize(normalize_prediction(pred), {})
    e = canonicalize(expected, {})
    if is_no_merchant(e) and is_no_merchant(p):
        return 1.0
    if is_no_merchant(e) or is_no_merchant(p):
        return 0.0
    pred_tokens = set(norm_key(p) for p in p.split() if norm_key(p))
    exp_tokens = set(norm_key(t) for t in e.split() if norm_key(t))
    if not pred_tokens and not exp_tokens:
        return 1.0
    if not pred_tokens or not exp_tokens:
        return 0.0
    overlap = len(pred_tokens & exp_tokens)
    precision = overlap / len(pred_tokens)
    recall = overlap / len(exp_tokens)
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)


def empty_metrics(predictions: list[str], expected: list[str]) -> dict[str, float]:
    """Precision/recall/F1 for detecting non-merchant (empty) outputs."""
    tp = fp = fn = 0
    for pred, exp in zip(predictions, expected, strict=True):
        pred_empty = is_no_merchant(normalize_prediction(pred))
        exp_empty = is_no_merchant(exp)
        if pred_empty and exp_empty:
            tp += 1
        elif pred_empty and not exp_empty:
            fp += 1
        elif not pred_empty and exp_empty:
            fn += 1
    precision = tp / (tp + fp) if (tp + fp) else 1.0
    recall = tp / (tp + fn) if (tp + fn) else 1.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0
    return {
        "empty_precision": precision,
        "empty_recall": recall,
        "empty_f1": f1,
        "false_merchant_count": fp,
        "missed_empty_count": fn,
    }


def merchant_metrics(
    predictions: list[str],
    expected: list[str],
    aliases: dict[str, str] | None = None,
) -> dict[str, float]:
    aliases = aliases or {}
    n = len(predictions)
    if n == 0:
        return {
            "count": 0,
            "exact_match_rate": 0.0,
            "normalized_match_rate": 0.0,
            "mean_token_f1": 0.0,
        }
    exact = sum(1 for p, e in zip(predictions, expected, strict=True) if exact_match(p, e, aliases))
    norm = sum(1 for p, e in zip(predictions, expected, strict=True) if normalized_match(p, e, aliases))
    f1s = [token_f1(p, e) for p, e in zip(predictions, expected, strict=True)]
    return {
        "count": n,
        "exact_match_rate": exact / n,
        "normalized_match_rate": norm / n,
        "mean_token_f1": sum(f1s) / n,
    }


def load_eval_descriptions(root: Path | None = None) -> set[str]:
    """All descriptions reserved for held-out eval files."""
    root = root or Path(__file__).parent
    out: set[str] = set()
    for name in ("eval_merchant.csv", "eval_non_merchant.csv", "eval_manual.json"):
        path = root / name
        if not path.exists():
            continue
        if path.suffix == ".json":
            import json

            data = json.loads(path.read_text(encoding="utf-8"))
            for row in data:
                out.add(row["description"].strip())
        else:
            with path.open(newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    out.add(row["description"].strip())
    return out