import frappe

def dry_run_cleanup():
    \"\"
    DRY RUN di esempio per verificare cosa verrebbe pulito.
    \"\"
    logs = frappe.get_all("Gara Log Operazioni", fields=["name"], limit=50)
    api_logs = frappe.get_all("API Log", fields=["name"], limit=50)
    return {
        "gara_log_operazioni": [l.name for l in logs],
        "api_log": [a.name for a in api_logs],
    }
