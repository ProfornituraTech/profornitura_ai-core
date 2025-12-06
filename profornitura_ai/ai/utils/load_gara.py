from typing import Any, Dict
import frappe

def load_gara(gara_name: str) -> Dict[str, Any]:
    doc = frappe.get_doc("Gara", gara_name)
    return {
        "name": doc.name,
        "cpv": getattr(doc, "cpv", None),
        "cig": getattr(doc, "cig", None),
        "importo_base": getattr(doc, "importo_base", 0),
        "scadenza_offerta": getattr(doc, "scadenza_offerta", None),
        "stazione_appaltante": getattr(doc, "stazione_appaltante", None),
        "richiede_sopralluogo": getattr(doc, "richiede_sopralluogo", 0),
        "richiede_soa": getattr(doc, "richiede_soa", 0),
        "richiede_anticipazione": getattr(doc, "richiede_anticipazione", 0),
        "lotto_numero": getattr(doc, "lotto_numero", None),
        "tipo_gara": getattr(doc, "tipo_gara", None),
    }
