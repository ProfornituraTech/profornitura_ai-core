
from __future__ import unicode_literals
import re
import frappe
from frappe.utils import now

SAFE_MODE = True
LOG_CHANNEL = "profornitura_ai_anac"

def get_logger():
    return frappe.logger(LOG_CHANNEL)

def validate_gara_compliance(doc, method=None):
    logger = get_logger()
    logger.info(f"[ANAC] Validazione gara {doc.name}")

    messages = []
    cig = (getattr(doc, "cig", "") or "").strip().upper()
    cpv = (getattr(doc, "cpv", "") or "").strip()

    if not cig or not re.fullmatch(r"[A-Z0-9]{10}", cig):
        messages.append(f"CIG non valido: {cig}")

    if not cpv or not re.fullmatch(r"[0-9]{8}-[0-9]", cpv):
        messages.append(f"CPV non valido: {cpv}")

    if messages:
        msg = " | ".join(messages)
        logger.warning(msg)
        if SAFE_MODE:
            frappe.msgprint(f"⚠️ ANAC Warning: {msg}", alert=True)
        else:
            frappe.throw(f"Errore ANAC: {msg}")
    else:
        logger.info(f"[ANAC] Gara {doc.name} conforme.")
