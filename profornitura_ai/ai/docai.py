import frappe

def run_docai(gara_name):
    \"\"
    Placeholder DocAI:
    - legge il DocType Gara
    - crea un DocAI Report minimamente popolato
    \"\"
    gara = frappe.get_doc("Gara", gara_name)

    report = frappe.new_doc("DocAI Report")
    report.gara = gara.name
    report.testo_estratto = "TESTO ESTRATTO (placeholder)"
    report.sezioni_json = "{}"
    report.insert(ignore_permissions=True)
    frappe.db.commit()
    return report.name
