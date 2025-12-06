from typing import Dict, Any, Tuple
import re
from ..config import GovernancePolicy

CIG_PATTERN = re.compile(r"^[A-Z0-9]{10}$")

def check_cig(cig: str | None) -> Tuple[bool, str]:
    if not cig:
        return False, "CIG mancante."
    if not CIG_PATTERN.match(cig):
        return False, "Formato CIG non valido."
    return True, "CIG valido."

def check_cpv(cpv: str | None) -> Tuple[bool, str]:
    if not cpv:
        return False, "CPV mancante."
    return True, "CPV presente (verifica whitelist lato DB)."

def governance_score(
    gara: Dict[str, Any],
    policy: GovernancePolicy,
) -> Tuple[bool, float, Dict[str, Any]]:
    score = 0.0
    reasons: Dict[str, Any] = {}

    if policy.enforce_cig_format:
        ok, msg = check_cig(gara.get("cig"))
        if not ok:
            score += 0.4
        reasons["cig"] = msg

    if policy.enforce_cpv_whitelist:
        ok, msg = check_cpv(gara.get("cpv"))
        if not ok:
            score += 0.3
        reasons["cpv"] = msg

    if gara.get("richiede_soa"):
        score += 0.3
        reasons["soa"] = "Richiesta SOA, non sempre compatibile con micro-SRL."

    score = max(0.0, min(score, 1.0))
    ok = score <= 0.5
    return ok, score, reasons
