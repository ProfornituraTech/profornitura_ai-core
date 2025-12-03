import frappe

def validate_cig(doc, method=None):
    \"\"
    Validazione CIG semplice:
    - obbligatorio
    - lunghezza 10 caratteri
    \"\"
    cig = getattr(doc, "cig", None)
    if not cig:
        frappe.throw("CIG obbligatorio per la Gara.")
    if len(cig) != 10:
        frappe.throw("CIG non valido: lunghezza diversa da 10 caratteri.")

def validate_cpv(doc, method=None):
    \"\"
    Validazione CPV semplice: solo obbligatorietà.
    \"\"
    cpv = getattr(doc, "cpv", None)
    if not cpv:
        frappe.throw("CPV obbligatorio per la Gara.")
