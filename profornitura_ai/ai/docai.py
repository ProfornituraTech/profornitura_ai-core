import frappe

def run_docai_for_gara(gara_name: str) -> str:
    """Placeholder DocAI.
    In M2/M3 verrà sostituito con:
    - estrazione PDF
    - parsing documenti
    - salvataggio in Report AI
    """
    logger = frappe.logger("profornitura_ai.docai")
    logger.info("DocAI placeholder eseguito per gara=%s", gara_name)
    return "DocAI placeholder completato per gara: {0}".format(gara_name)
