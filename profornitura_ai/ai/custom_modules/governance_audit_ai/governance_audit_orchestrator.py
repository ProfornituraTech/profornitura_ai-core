"""GOVERNANCE & AUDIT AI v1 – Orchestrator (Blueprint)

Scopo:
- eseguire un meta-audit di sicurezza, permessi e salute del sistema
- incrociare risultati di altri report locali (audit, fix, compliance)
- generare un "governance snapshot" centrale.

Al momento:
- legge solo pochi elementi di base da ERPNext
- e si affida a report locali se presenti.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Any

from api_client import FrappeClient
from config_super_suite import SUPER_SUITE_SAFE_MODE, SUPER_SUITE_EXECUTE, REPORT_DIR_DEFAULT


def _load_report(prefix: str) -> Dict[str, Any]:
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


def run_governance_audit() -> Dict[str, Any]:
    client = FrappeClient()

    # Info base system
    try:
        ss = client.get_single("System Settings")
        system_data = ss.get("data", ss)
    except Exception:
        system_data = {}

    # Carichiamo altri report se esistono
    audit_full = _load_report("ERP_AUDIT_FULL")
    verify_core = _load_report("VERIFY_CORE_V1")
    compliance = _load_report("COMPLIANCE_GUARDIAN_V1")
    auto_fix_m3 = _load_report("AUTO_FIX_M3")

    snapshot = {
        "meta": {
            "safe_mode": SUPER_SUITE_SAFE_MODE,
            "execute_mode": SUPER_SUITE_EXECUTE,
        },
        "system_settings": {
            "session_expiry": system_data.get("session_expiry"),
            "deny_multiple_sessions": system_data.get("deny_multiple_sessions"),
        },
        "external_reports": {
            "has_audit_full": bool(audit_full),
            "has_verify_core": bool(verify_core),
            "has_compliance": bool(compliance),
            "has_auto_fix_m3": bool(auto_fix_m3),
        },
    }
    return snapshot


def main():
    client = FrappeClient()
    print("\n==============================================")
    print(" PROFORNITURA AI – GOVERNANCE & AUDIT AI v1")
    print("==============================================\n")    

    report = run_governance_audit()
    json_path, md_path = client.save_report("GOVERNANCE_AUDIT_AI_V1", report)

    print("\n🎯 REPORT GOVERNANCE & AUDIT AI V1 SALVATO:")
    print(f"   JSON: {json_path}")
    print(f"   MD:   {md_path}")
    print("\n✅ COMPLETATO (blueprint).\n")


if __name__ == "__main__":
    main()
