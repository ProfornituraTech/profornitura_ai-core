import frappe

def run_auto_cleanup(dry_run: bool = True) -> dict:
    """Placeholder AutoCleanup.
    M2/M3: pulizia log vecchi, DocAI temporanei, ecc.
    """
    logger = frappe.logger("profornitura_ai.cleanup")
    mode = "DRY_RUN" if dry_run else "EXECUTE"
    logger.info("Esecuzione AutoCleanup placeholder in modalità %s", mode)

    return {
        "mode": mode,
        "status": "placeholder",
        "deleted_records": 0,
        "notes": "AutoCleanup reale verrà implementato in M2/M3."
    }
