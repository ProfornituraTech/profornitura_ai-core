import frappe

def evaluate_gara_for_company(gara_name: str, company: str = "Profornitura Italia SRL") -> dict:
    """Placeholder AutoDecisionAI.
    Ritorna uno score fittizio e un messaggio loggato.
    M2/M3 sostituiranno questa logica con quella reale.
    """
    logger = frappe.logger("profornitura_ai.decisionai")
    logger.info("Esecuzione AutoDecisionAI placeholder per gara=%s company=%s", gara_name, company)

    return {
        "gara": gara_name,
        "company": company,
        "score": 75,
        "status": "placeholder",
        "reason": "AutoDecisionAI pipeline ancora da implementare (M2/M3)."
    }
