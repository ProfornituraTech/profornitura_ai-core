import frappe

def check_upcoming_deadlines(days_ahead: int = 7) -> list:
    """Placeholder TimelineAI.
    In M2/M3: cercherà le scadenze delle gare entro X giorni.
    Ora ritorna solo una lista vuota.
    """
    logger = frappe.logger("profornitura_ai.timeline")
    logger.info("Timeline placeholder: controllo scadenze nei prossimi %s giorni", days_ahead)
    return []
