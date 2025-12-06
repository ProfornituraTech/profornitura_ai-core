"""ZERO-LIQUIDITY ENGINE v2 – Blueprint

Versione concettuale avanzata del motore Zero Liquidità.

- legge risultati dell'AI Parser 2.0 (se presenti)
- applica regole più sofisticate (per ora, demo)
- produce uno score di compatibilità più dettagliato.

Al momento:
- non scrive su ERPNext
- crea solo un report di analisi.
"""
from __future__ import annotations

from typing import Dict, Any, List

from api_client import FrappeClient
from config_super_suite import SUPER_SUITE_SAFE_MODE, SUPER_SUITE_EXECUTE


def run_zero_liquidity_engine_v2() -> Dict[str, Any]:
    client = FrappeClient()

    # Per ora, usiamo la stessa base di Gara del V1 ma con struttura arricchita
    try:
        raw = client.list_docs(
            "Gara",
            fields=["name", "oggetto", "importo_base", "data_scadenza"],
            limit=100,
        )
        gare = raw.get("data", raw) or []
    except Exception:
        gare = []

    results: List[Dict[str, Any]] = []
    for g in gare:
        name = g.get("name")
        if not name:
            continue
        base = float(g.get("importo_base") or 0)
        score = 50.0
        notes = []

        if base <= 0:
            score -= 15
            notes.append("Importo non valido per valutazione.")
        elif base < 10000:
            score += 15
            notes.append("Importo contenuto: ideale per zero liquidità.")
        elif base > 200000:
            score -= 15
            notes.append("Importo elevato: zero liquidità più rischiosa.")

        if score < 0:
            score = 0.0
        if score > 100:
            score = 100.0

        results.append(
            {
                "gara": name,
                "oggetto": g.get("oggetto"),
                "importo_base": base,
                "score_zero_liquidity_v2": round(score, 2),
                "notes": "; ".join(notes) or "Analisi base demo.",
            }
        )

    return {
        "meta": {
            "safe_mode": SUPER_SUITE_SAFE_MODE,
            "execute_mode": SUPER_SUITE_EXECUTE,
        },
        "stats": {
            "gare_analizzate": len(results),
        },
        "results": results,
    }


def main():
    client = FrappeClient()

    print("\n==============================================")
    print(" PROFORNITURA AI – ZERO-LIQUIDITY ENGINE v2")
    print("==============================================\n")
    print("Modalità:")
    print(f"  SUPER_SUITE_SAFE_MODE = {SUPER_SUITE_SAFE_MODE}")
    print(f"  SUPER_SUITE_EXECUTE   = {SUPER_SUITE_EXECUTE}\n")

    print("1) Analisi avanzata compatibilità zero liquidità...")
    report = run_zero_liquidity_engine_v2()
    json_path, md_path = client.save_report("ZERO_LIQUIDITY_V2", report)

    print("\n🎯 REPORT ZERO-LIQUIDITY V2 SALVATO:")
    print(f"   JSON: {json_path}")
    print(f"   MD:   {md_path}")
    print("\n✅ COMPLETATO (modalità blueprint).\n")


if __name__ == "__main__":
    main()
