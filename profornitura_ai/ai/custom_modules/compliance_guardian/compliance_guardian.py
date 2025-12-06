"""COMPLIANCE & ANAC GUARDIAN v1 – Blueprint

Scopo:
- incrociare le gare con semplici regole di conformità
- produrre un semaforo di rischio (verde/giallo/rosso)
- salvare un report locale di "Compliance Snapshot".

In questa versione:
- non leggiamo database ANAC reali
- non applichiamo regole legali vere
- ma strutturiamo il formato di output che in futuro potrà essere popolato
  da un motore legale/ANAC reale.
"""
from __future__ import annotations

from typing import Dict, Any, List

from api_client import FrappeClient
from config_super_suite import SUPER_SUITE_SAFE_MODE, SUPER_SUITE_EXECUTE


def run_compliance_guardian() -> Dict[str, Any]:
    client = FrappeClient()

    try:
        raw = client.list_docs(
            "Gara",
            fields=["name", "oggetto", "cig", "cpv", "data_scadenza"],
            limit=200,
        )
        gare = raw.get("data", raw) or []
    except Exception:
        gare = []

    items: List[Dict[str, Any]] = []
    for g in gare:
        risk_level = "GREEN"
        notes = []

        if not g.get("cig"):
            risk_level = "RED"
            notes.append("CIG mancante.")
        if not g.get("cpv"):
            if risk_level != "RED":
                risk_level = "YELLOW"
            notes.append("CPV mancante.")

        items.append(
            {
                "gara": g.get("name"),
                "oggetto": g.get("oggetto"),
                "cig": g.get("cig"),
                "cpv": g.get("cpv"),
                "risk_level": risk_level,
                "notes": "; ".join(notes) or "Controlli demo.",
            }
        )

    return {
        "meta": {
            "safe_mode": SUPER_SUITE_SAFE_MODE,
            "execute_mode": SUPER_SUITE_EXECUTE,
        },
        "stats": {
            "gare_verificate": len(items),
        },
        "items": items,
    }


def main():
    client = FrappeClient()
    print("\n==============================================")
    print(" PROFORNITURA AI – COMPLIANCE & ANAC GUARDIAN v1")
    print("==============================================\n")

    report = run_compliance_guardian()
    json_path, md_path = client.save_report("COMPLIANCE_GUARDIAN_V1", report)

    print("\n🎯 REPORT COMPLIANCE GUARDIAN V1 SALVATO:")
    print(f"   JSON: {json_path}")
    print(f"   MD:   {md_path}")
    print("\n✅ COMPLETATO (blueprint).\n")


if __name__ == "__main__":
    main()
