from typing import Dict, Any

def safe_float(value, default: float = 0.0) -> float:
    try:
        return float(value)
    except Exception:
        return default

def merge_scores(*scores: float) -> float:
    valid = [s for s in scores if s is not None]
    return sum(valid) / len(valid) if valid else 0.0

def result_dict(
    *,
    entity_name: str,
    gara_name: str,
    compatible: bool,
    risk_score: float,
    reasons: Dict[str, Any],
) -> Dict[str, Any]:
    return {
        "entity": entity_name,
        "gara": gara_name,
        "compatible": compatible,
        "risk_score": risk_score,
        "reasons": reasons,
    }
