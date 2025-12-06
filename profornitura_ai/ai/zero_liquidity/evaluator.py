from typing import Dict, Any, Tuple
from ..config import EntityProfile, ZeroLiquidityPolicy
from ..utils.helpers import safe_float

def evaluate_financial_compatibility(
    entity: EntityProfile,
    gara: Dict[str, Any],
    policy: ZeroLiquidityPolicy,
) -> Tuple[bool, float, Dict[str, Any]]:
    importo = safe_float(gara.get("importo_base"), 0.0)

    score = 0.0
    reasons: Dict[str, Any] = {}

    if importo <= 0:
        reasons["importo"] = "Importo non definito, considerata neutra."
    elif importo <= 50000:
        score += 0.1
        reasons["importo"] = "Importo basso, adatto a SRL giovane."
    elif importo <= 200000:
        score += 0.3
        reasons["importo"] = "Importo medio, richiede attenzione ma gestibile."
    else:
        score += 0.6
        reasons["importo"] = "Importo alto, possibile impatto su cassa."

    if policy.allow_anticipo_fattura:
        score -= 0.1
        reasons["anticipo_fattura"] = "Uso anticipo fattura ammesso."

    if gara.get("richiede_anticipazione"):
        score += 0.2
        reasons["anticipazione"] = "Richiesta anticipazione, verifica coperture."

    if entity.is_startup:
        score += 0.1
        reasons["startup"] = "SRL startup, rating bancario da verificare."

    score = max(0.0, min(score, 1.0))
    compatible = score <= entity.max_risk_score
    return compatible, score, reasons
