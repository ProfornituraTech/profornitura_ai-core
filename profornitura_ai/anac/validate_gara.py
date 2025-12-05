import frappe

def validate_gara_compliance(gara_name: str) -> dict:
    """Placeholder ANAC compliance.
    M2/M3: validazione CIG, CPV, requisiti, ecc.
    """
    logger = frappe.logger("profornitura_ai.anac")
    logger.info("Validazione ANAC placeholder per gara=%s", gara_name)
    return {
        "gara": gara_name,
        "compliant": True,
        "details": "Validazione ANAC placeholder – da implementare."
    }
