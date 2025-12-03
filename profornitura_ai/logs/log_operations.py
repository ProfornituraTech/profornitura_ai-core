import frappe
from frappe.utils import now

def log_gara_update(doc, method=None):
    \"\"
    Crea una riga in Gara Log Operazioni ad ogni update della Gara.
    Richiede un DocType 'Gara Log Operazioni' con campi:
    - gara (Link)
    - operazione (Data/Ora)
    - utente
    - descrizione
    \"\"
    try:
        log = frappe.new_doc("Gara Log Operazioni")
        log.gara = doc.name
        log.operazione = now()
        log.utente = frappe.session.user
        log.descrizione = f"Aggiornamento Gara (workflow_state={getattr(doc, 'workflow_state', '')})"
        log.insert(ignore_permissions=True)
        frappe.db.commit()
    except Exception as e:
        frappe.logger().error(f"Errore log_gara_update: {e}")
