import frappe

def calculate_score(gara_name):
    \"\"
    Placeholder AutoDecisionAI:
    - calcola uno score base
    - setta campi su Gara se esistono
    \"\"
    gara = frappe.get_doc("Gara", gara_name)

    score = 75.0
    risultato = "Idonea" if score >= 60 else "Non idonea"

    if hasattr(gara, "autodecisionai_punteggio"):
        gara.autodecisionai_punteggio = score
    if hasattr(gara, "autodecisionai_motivazione"):
        gara.autodecisionai_motivazione = "Valutazione automatica placeholder."
    if hasattr(gara, "idonea_per_srl_nuova"):
        gara.idonea_per_srl_nuova = (risultato == "Idonea")

    gara.save(ignore_permissions=True)
    frappe.db.commit()
    return score, risultato
