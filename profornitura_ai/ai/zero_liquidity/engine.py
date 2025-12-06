from typing import Dict, Any
from ..config import DEFAULT_ENTITY, DEFAULT_ZERO_LIQ_POLICY
from ..utils.entity_profile import load_entity_profile
from ..utils.helpers import result_dict

def evaluate_zero_liquidity(
    gara: Dict[str, Any],
    entity_name: str = None,
) -> Dict[str, Any]:
    entity = load_entity_profile(entity_name) if entity_name else DEFAULT_ENTITY
    compatible, risk_score, reasons = evaluate_financial_compatibility(
        entity, gara, DEFAULT_ZERO_LIQ_POLICY  # type: ignore[name-defined]
    )
    return result_dict(
        entity_name=entity.name,
        gara_name=gara.get("name"),
        compatible=compatible,
        risk_score=risk_score,
        reasons=reasons,
    )
