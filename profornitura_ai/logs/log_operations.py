import frappe
from typing import Optional, Dict, Any

def log_gara_operation(gara_name: str, action: str, meta: Optional[Dict[str, Any]] = None):
    """Placeholder Log Engine.
    Registra un semplice log su logger Frappe.
    """
    logger = frappe.logger("profornitura_ai.logs")
    logger.info("LOG_GARA | gara=%s | action=%s | meta=%s", gara_name, action, meta or {})
