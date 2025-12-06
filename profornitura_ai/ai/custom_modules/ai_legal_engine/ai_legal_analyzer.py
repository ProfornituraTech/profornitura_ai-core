"""AI LEGAL ENGINE v1 – Blueprint

Analisi legale automatizzata (concettuale):

- in questa versione NON effettua vera consulenza legale
- NON sostituisce un avvocato
- NON esce dall'ambito demo/blueprint

Scopo attuale:
- definire il formato di output, con evidenza di clausole critiche.
"""
from __future__ import annotations

from typing import Dict, Any, List

from api_client import FrappeClient
from config_super_suite import SUPER_SUITE_SAFE_MODE, SUPER_SUITE_EXECUTE


def run_ai_legal_analyzer() -> Dict[str, Any]:
    client = FrappeClient()

    try:
        raw = client.list_docs(
            "Gara",
            fields=["name", "oggetto"],
            limit=50,
        )
        gare = raw.get("data", raw) or []
    except Exception:
        gare = []

    analyses: List[Dict[str, Any]] = []
    for g in gare:
        analyses.append(
            {
                "gara": g.get("name"),
                "oggetto": g.get("oggetto"),
                "risk_level": "UNKNOWN_DEMO",
                "issues": [
                    "Analisi legale non implementata (blueprint)."
                ],
            }
        )

    return {
        "meta": {
            "safe_mode": SUPER_SUITE_SAFE_MODE,
            "execute_mode": SUPER_SUITE_EXECUTE,
        },
        "stats": {
            "gare_analizzate": len(analyses),
        },
        "analyses": analyses,
    }


def main():
    client = FrappeClient()
    print("\n==============================================")
    print(" PROFORNITURA AI – AI LEGAL ENGINE v1 (BLUEPRINT)")
    print("==============================================\n")

    report = run_ai_legal_analyzer()
    json_path, md_path = client.save_report("AI_LEGAL_ENGINE_V1", report)

    print("\n🎯 REPORT AI LEGAL ENGINE V1 SALVATO:")
    print(f"   JSON: {json_path}")
    print(f"   MD:   {md_path}")
    print("\n✅ COMPLETATO (blueprint).\n")


if __name__ == "__main__":
    main()
