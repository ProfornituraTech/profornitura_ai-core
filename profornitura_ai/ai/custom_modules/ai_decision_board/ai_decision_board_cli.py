"""AI DECISION BOARD CLI – Blueprint

Piccola CLI che legge vari report (autopilot, zero liquidity, compliance, entity)
e mostra un riassunto testuale delle decisioni strategiche consigliate.

In futuro:
- diventera' un vero dashboard ERPNext + interfaccia web.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Any

from config_super_suite import REPORT_DIR_DEFAULT


def _load(prefix: str) -> Dict[str, Any]:
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


def main():
    print("\n==============================================")
    print(" PROFORNITURA AI – AI DECISION BOARD (CLI)")
    print("==============================================\n")    

    autopilot = _load("TENDER_AUTOPILOT_V1")
    entity = _load("ENTITY_ENGINE_V1")
    zero_liq = _load("ZERO_LIQUIDITY_V2")
    compliance = _load("COMPLIANCE_GUARDIAN_V1")

    print("[Decision Board Snapshot]\n")

    if autopilot:
        stats = autopilot.get("stats", {})
        print("- Autopilot:")
        print("  gare considerate:", stats.get("gare_considerate"))
        print("  suggerimenti:", stats.get("suggerimenti"))
    else:
        print("- Autopilot: nessun report trovato.")

    if entity:
        stats = entity.get("stats", {})
        print("- Entity Engine:")
        print("  gare:", stats.get("gare"))
        print("  entità:", stats.get("entities"))
    else:
        print("- Entity Engine: nessun report trovato.")

    if zero_liq:
        stats = zero_liq.get("stats", {})
        print("- ZeroLiquidity v2:")
        print("  gare analizzate:", stats.get("gare_analizzate"))
    else:
        print("- ZeroLiquidity v2: nessun report trovato.")

    if compliance:
        stats = compliance.get("stats", {})
        print("- Compliance Guardian:")
        print("  gare verificate:", stats.get("gare_verificate"))
    else:
        print("- Compliance Guardian: nessun report trovato.")

    print("\n(Questo è un dashboard testuale. In futuro diventerà UI web/ERPNext.)\n")


if __name__ == "__main__":
    main()
