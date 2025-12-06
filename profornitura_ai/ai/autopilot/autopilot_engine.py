from typing import Dict, Any, List
import frappe
from ..config import DEFAULT_AUTOPILOT_CONFIG, DEFAULT_GOVERNANCE_POLICY
from ..utils.load_gara import load_gara
from ..utils.entity_profile import load_entity_profile
from ..utils.log import log_ai_event
from ..zero_liquidity.engine import evaluate_zero_liquidity
from ..governance.validator import governance_score
from ..decision.decision_engine import build_decision
from ..timeline.timeline_engine import upsert_gara_deadline_event

def _evaluate_single_gara(gara_name: str, entity_name: str = None) -> Dict[str, Any]:
    gara = load_gara(gara_name)
    entity = load_entity_profile(entity_name)
    zero_liq_res = evaluate_zero_liquidity(gara, entity.name)
    gov_ok, gov_score, gov_reasons = governance_score(gara, DEFAULT_GOVERNANCE_POLICY)

    gov_res = {
        "ok": gov_ok,
        "risk_score": gov_score,
        "reasons": gov_reasons,
    }

    decision = build_decision(zero_liq_res=zero_liq_res, governance_res=gov_res)
    return decision

def run_gara_autopilot(
    entity_name: str = None,
    gara_list: List[str] | None = None,
    config=DEFAULT_AUTOPILOT_CONFIG,
) -> List[Dict[str, Any]]:
    """Esegue l'autopilot sulle gare indicate o su tutte le gare 'Da Valutare'."""
    if gara_list is None:
        gara_list = [
            x.name
            for x in frappe.get_all(
                "Gara",
                filters={"workflow_state": ["in", ["Da Valutare", "Nuova"]]},
                pluck="name",
            )
        ]

    results: List[Dict[str, Any]] = []
    for name in gara_list:
        decision = _evaluate_single_gara(name, entity_name)
        results.append(decision)

        if not config.dry_run:
            frappe.db.set_value("Gara", name, "ai_raccomandazione", decision["label"])
            frappe.db.set_value("Gara", name, "ai_rischio", decision["risk_score"])

        upsert_gara_deadline_event(load_gara(name))
        log_ai_event("AUTOPILOT_DECISION", decision)

    return results
