
from __future__ import unicode_literals
import frappe
from frappe.utils import now

SAFE_MODE = True
LOG_CHANNEL = "profornitura_ai_audit"

def get_logger():
    return frappe.logger(LOG_CHANNEL)

def _log(doc, action, details=""):
    logger = get_logger()
    try:
        entry = frappe.get_doc({
            "doctype": "Gara Operation Log",
            "gara": doc.name,
            "azione": action,
            "dettagli": details,
            "utente": frappe.session.user,
            "timestamp": now(),
        })
        entry.insert(ignore_permissions=True)
        logger.info(f"[AUDIT] {action} registrato per {doc.name}")
    except Exception as e:
        logger.error(f"[AUDIT ERROR] {e}")

def log_gara_insert(doc, method=None):
    _log(doc, "Insert", "Gara creata")

def log_gara_update(doc, method=None):
    _log(doc, "Update", "Gara aggiornata")

def log_gara_cancel(doc, method=None):
    _log(doc, "Cancel", "Gara annullata")
