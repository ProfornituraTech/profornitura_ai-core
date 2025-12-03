import frappe

def check_upcoming_deadlines():
    \"\"
    Esempio di scheduler TimelineAI:
    invia un'email di promemoria per le scadenze aperte.
    \"\"
    scadenze = frappe.get_all(
        "Scadenza Gara",
        filters={"notifica_inviata": 0},
        fields=["name", "gara", "data_scadenza"]
    )

    for s in scadenze:
        subject = f"Promemoria scadenza gara: {s.get('gara')}"
        message = f"La scadenza {s.get('name')} per la gara {s.get('gara')} è il {s.get('data_scadenza')}."
        frappe.sendmail(
            recipients=[frappe.session.user],
            subject=subject,
            message=message
        )
        frappe.db.set_value("Scadenza Gara", s.get("name"), "notifica_inviata", 1)
