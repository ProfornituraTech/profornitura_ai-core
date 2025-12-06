from typing import Dict, Any
from ..utils.helpers import merge_scores

def build_decision(
    *,
    zero_liq_res: Dict[str, Any],
    governance_res: Dict[str, Any],
) -> Dict[str, Any]:
    risk_score = merge_scores(
        zero_liq_res.get("risk_score"),
        governance_res.get("risk_score"),
    )

    if risk_score <= 0.25:
        label = "PARTECIPA"
    elif risk_score <= 0.5:
        label = "VALUTA_CON_ATTENZIONE"
    else:
        label = "NON_PARTECIPARE"

    return {
        "entity": zero_liq_res.get("entity"),
        "gara": zero_liq_res.get("gara"),
        "risk_score": risk_score,
        "label": label,
        "zero_liq": zero_liq_res,
        "governance": governance_res,
    }
