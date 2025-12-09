
from __future__ import unicode_literals
import frappe
from frappe.utils import nowdate, add_days

SAFE_MODE = True
REMINDER_DAYS = 3
LOG_CHANNEL = "profornitura_ai_timeline"

def get_logger():
    return frappe.logger(LOG_CHANNEL)

def send_deadline_reminders():
    logger = get_logger()
    today = nowdate()
    target = add_days(today, REMINDER_DAYS)

    deadlines = frappe.get_all(
        "Scadenza Gara",
        filters={"data_scadenza": ["between", [today, target]], "notified": 0},
        fields=["name", "gara", "data_scadenza", "tipo_scadenza", "notify_cto", "notify_bid_manager"]
    )

    for d in deadlines:
        logger.info(f"[TimelineAI] Reminder → {d}")
        frappe.db.set_value("Scadenza Gara", d["name"], "notified", 1)
