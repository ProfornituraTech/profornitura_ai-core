import frappe
from datetime import datetime
from typing import Dict, Any

def upsert_gara_deadline_event(gara: Dict[str, Any]) -> None:
    if not gara.get("scadenza_offerta"):
        return

    deadline = gara["scadenza_offerta"]
    if isinstance(deadline, str):
        deadline = datetime.fromisoformat(deadline)

    ref = f"GARA-DEADLINE-{gara['name']}"
    existing = frappe.db.get_value("Timeline Event", {"reference": ref}, "name")
    data = {
        "doctype": "Timeline Event",
        "reference": ref,
        "title": f"Scadenza offerta gara {gara['name']}",
        "event_datetime": deadline,
        "gara": gara["name"],
    }

    if existing:
        doc = frappe.get_doc("Timeline Event", existing)
        doc.update(data)
        doc.save(ignore_permissions=True)
    else:
        frappe.get_doc(data).insert(ignore_permissions=True)
