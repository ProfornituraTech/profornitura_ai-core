"""ONE-CLICK GARA PACK v1 – Planner (Blueprint)

Scopo:
- definire il "piano di partecipazione" per ogni gara
- associare documenti richiesti
- indicare quali devono essere firmati
- salvare un report locale con la check-list.

In futuro:
- questo modulo creerà Doctype "Gara Participation Blueprint" su ERPNext
- attiverà i flussi di generazione documenti e firma digitale.
"""
from __future__ import annotations

from typing import Dict, Any, List

from api_client import FrappeClient
from config_super_suite import SUPER_SUITE_SAFE_MODE, SUPER_SUITE_EXECUTE


REQUIRED_DOCS_DEFAULT = [
    {"document_type": "DGUE", "needs_signature": True},
    {"document_type": "Offerta Tecnica", "needs_signature": True},
    {"document_type": "Offerta Economica", "needs_signature": True},
    {"document_type": "Dichiarazioni Sostitutive", "needs_signature": True},
]


def build_one_click_plan() -> Dict[str, Any]:
    client = FrappeClient()

    try:
        raw = client.list_docs(
            "Gara",
            fields=["name", "oggetto", "importo_base", "data_scadenza"],
            limit=100,
        )
        gare = raw.get("data", raw) or []
    except Exception:
        gare = []

    blueprints: List[Dict[str, Any]] = []
    for g in gare:
        bp = {
            "gara": g.get("name"),
            "oggetto": g.get("oggetto"),
            "docs": REQUIRED_DOCS_DEFAULT,
            "portal": "N/D",  # in futuro: Sintel / Consip / MEPA / TED
            "status": "PLANNED_ONLY",
        }
        blueprints.append(bp)

    return {
        "meta": {
            "safe_mode": SUPER_SUITE_SAFE_MODE,
            "execute_mode": SUPER_SUITE_EXECUTE,
        },
        "stats": {
            "gare": len(blueprints),
        },
        "blueprints": blueprints,
    }


def main():
    client = FrappeClient()
    print("\n==============================================")
    print(" PROFORNITURA AI – ONE-CLICK GARA PLANNER v1")
    print("==============================================\n")

    report = build_one_click_plan()
    json_path, md_path = client.save_report("ONE_CLICK_GARA_V1", report)

    print("\n🎯 REPORT ONE-CLICK GARA V1 SALVATO:")
    print(f"   JSON: {json_path}")
    print(f"   MD:   {md_path}")
    print("\n✅ COMPLETATO (pianificazione, nessuna azione su ERPNext).\n")


if __name__ == "__main__":
    main()
