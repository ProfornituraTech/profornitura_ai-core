"""TENDER AUTOPILOT ENGINE v1 – Orchestrator (SAFE MODE / BLUEPRINT)

Obiettivo:
- Leggere gare da ERPNext
- Leggere (se esistono) output di:
  - Entity Engine v1
  - ZeroLiquidityEngine
  - Compliance Guardian (quando sarà implementato)
- Generare un piano di azioni automatiche (partecipare / non partecipare / approfondire)

Modalità attuale:
- SOLO lettura (usa SUPER_SUITE_SAFE_MODE)
- NON scrive su ERPNext
- crea un report di pianificazione in ./reports.

In futuro:
- potrà creare record "Autopilot Recommendation" su ERPNext
- potrà orchestrare blueprint di partecipazione, firma digitale, ecc.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from api_client import FrappeClient
from config_super_suite import SUPER_SUITE_SAFE_MODE, SUPER_SUITE_EXECUTE, REPORT_DIR_DEFAULT


def _load_local_report(prefix: str) -> Dict[str, Any]:
    """Carica l'ultimo report locale che inizia con `prefix` nella cartella reports.
    Se non trovato, ritorna un dict vuoto.
    """
    reports_dir = Path(REPORT_DIR_DEFAULT)
    if not reports_dir.exists():
        return {}
    candidates = sorted(reports_dir.glob(f"{prefix}_*.json"), reverse=True)
    if not candidates:
        return {}
    try:
        with candidates[0].open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def build_autopilot_plan() -> Dict[str, Any]:
    client = FrappeClient()

    # 1) Leggi alcune gare da ERPNext (se possibile)
    try:
        raw_gare = client.list_docs(
            "Gara",
            fields=["name", "oggetto", "importo_base", "data_scadenza"],
            limit=200,
        )
        gare = raw_gare.get("data", raw_gare) or []
    except Exception:
        gare = []

    # 2) Carica eventuali output di altri engine
    entity_engine = _load_local_report("ENTITY_ENGINE_V1")
    zero_liq = _load_local_report("ZERO_LIQUIDITY_ENGINE")
    compliance = _load_local_report("COMPLIANCE_GUARDIAN_V1")  # previsto in futuro

    # Mappature snelle
    best_by_gara = entity_engine.get("best_by_gara", {})
    zero_liq_index: Dict[str, Any] = {}
    for item in zero_liq.get("results", []):
        gara_name = item.get("gara") or item.get("name")
        if gara_name:
            zero_liq_index[gara_name] = item

    # 3) Costruisci un piano autopilot
    autoplan: List[Dict[str, Any]] = []
    for g in gare:
        name = g.get("name")
        rec: Dict[str, Any] = {
            "gara": name,
            "oggetto": g.get("oggetto"),
            "importo_base": g.get("importo_base"),
            "data_scadenza": g.get("data_scadenza"),
            "entity_suggested": None,
            "zero_liq_score": None,
            "decision": "REVIEW",  # PARTICIPATE / SKIP / REVIEW
            "reason": [],
        }

        # Suggerimento entità (Entity Engine)
        if name in best_by_gara:
            b = best_by_gara[name]
            rec["entity_suggested"] = b.get("best_entity_name") or b.get("best_entity")
            if b.get("can_participate"):
                rec["reason"].append("Entity Engine: entità idonea.")
            else:
                rec["reason"].append("Entity Engine: entità NON idonea.")

        # Zero liquidity
        if name in zero_liq_index:
            zl = zero_liq_index[name]
            score_zl = zl.get("score_zero_liquidity") or zl.get("score")
            rec["zero_liq_score"] = score_zl
            if score_zl is not None and score_zl >= 70:
                rec["reason"].append("ZeroLiquidityEngine: alta compatibilità zero liquidità.")
            elif score_zl is not None and score_zl < 40:
                rec["reason"].append("ZeroLiquidityEngine: bassa compatibilità zero liquidità.")

        # Decisione demo (solo logica di esempio)
        # In futuro: includere Compliance Guardian + AI Legal Engine
        if rec["zero_liq_score"] and rec["zero_liq_score"] >= 70 and rec["entity_suggested"]:
            rec["decision"] = "PARTICIPATE"
        elif rec["zero_liq_score"] and rec["zero_liq_score"] < 40:
            rec["decision"] = "SKIP"
        else:
            rec["decision"] = "REVIEW"

        rec["reason"] = "; ".join(rec["reason"])
        autoplan.append(rec)

    return {
        "meta": {
            "safe_mode": SUPER_SUITE_SAFE_MODE,
            "execute_mode": SUPER_SUITE_EXECUTE,
        },
        "stats": {
            "gare_considerate": len(gare),
            "suggerimenti": len(autoplan),
        },
        "plan": autoplan,
    }


def main():
    client = FrappeClient()

    print("\n==============================================")
    print(" PROFORNITURA AI – TENDER AUTOPILOT ENGINE v1")
    print("==============================================\n")
    print("Modalità corrente:")
    print(f"  SUPER_SUITE_SAFE_MODE = {SUPER_SUITE_SAFE_MODE}")
    print(f"  SUPER_SUITE_EXECUTE   = {SUPER_SUITE_EXECUTE}")
    if SUPER_SUITE_SAFE_MODE:
        print("  => SOLO PIANIFICAZIONE (nessuna scrittura su ERPNext)\n")    

    print("1) Costruzione piano autopilot gare...")
    report = build_autopilot_plan()
    json_path, md_path = client.save_report("TENDER_AUTOPILOT_V1", report)

    print("\n🎯 REPORT TENDER AUTOPILOT v1 SALVATO:")
    print(f"   JSON: {json_path}")
    print(f"   MD:   {md_path}")
    print("\n✅ COMPLETATO (modalità blueprint / sola lettura).\n")


if __name__ == "__main__":
    main()
