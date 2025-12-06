from typing import Any, Dict
import frappe

def log_ai_event(event_type: str, details: Dict[str, Any]) -> None:
    """
    Logga un evento AI su Doctype `AI Log` se esiste, altrimenti nei log standard di Frappe.
    """
    try:
        frappe.get_doc(
            {
                "doctype": "AI Log",
                "event_type": event_type,
                "payload": frappe.as_json(details),
            }
        ).insert(ignore_permissions=True)
    except Exception:
        frappe.logger("profornitura_ai").info(f"[AI-LOG] {event_type}: {details}")
