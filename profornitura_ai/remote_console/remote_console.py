import frappe
import io
import contextlib
from typing import Optional, Dict, Any

MASTER_PASSWORD = "PROFORNITURA2025!"  # Cambia qui se vuoi aggiornarla

ALLOWED_BUILTINS = {
    "len": len,
    "range": range,
    "min": min,
    "max": max,
    "sum": sum,
    "print": print,
}

def _run_preset(preset: str) -> str:
    from . import diagnostics_runner
    preset = (preset or "").strip().lower()

    if preset == "install_check":
        return diagnostics_runner.install_check()
    if preset == "doctype_check":
        return diagnostics_runner.doctype_check()
    if preset == "module_check":
        return diagnostics_runner.module_check()
    if preset == "full_check":
        return diagnostics_runner.full_check()

    return f"Preset sconosciuto: {preset!r}. Usa: install_check, doctype_check, module_check, full_check."


@frappe.whitelist(methods=["GET", "POST"], allow_guest=False)
def run(password: str, code: Optional[str] = None, preset: Optional[str] = None) -> Dict[str, Any]:
    """
    Remote Console sicura per Profornitura AI.

    - Richiede autenticazione Frappe (utente loggato o API Key/Secret)
    - Richiede password segreta (MASTER_PASSWORD)
    - Permette di eseguire:
        * codice arbitrario (parametro `code`)
        * diagnostiche predefinite (parametro `preset`)
    """

    if password != MASTER_PASSWORD:
        frappe.throw("Password non valida per Remote Console.", frappe.PermissionError)

    # Se è stato richiesto un preset, eseguo quello
    if preset:
        output = _run_preset(preset)
        return {
            "ok": True,
            "output": output,
            "error": None,
        }

    if not code:
        return {
            "ok": False,
            "output": "",
            "error": "Nessun codice da eseguire. Specifica `code` o `preset`.",
        }

    # Namespace controllato
    local_ctx: Dict[str, Any] = {
        "frappe": frappe,
    }

    # Builtins limitati
    safe_builtins = ALLOWED_BUILTINS.copy()
    local_ctx["__builtins__"] = safe_builtins

    stdout = io.StringIO()
    stderr = io.StringIO()
    error_text: Optional[str] = None

    try:
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            exec(code, local_ctx, local_ctx)  # noqa: S102
    except Exception as e:
        error_text = f"{type(e).__name__}: {e}"

    out_text = stdout.getvalue()
    err_text = stderr.getvalue()

    if error_text and err_text:
        error_text = error_text + "\n" + err_text
    elif not error_text:
        error_text = err_text or None

    return {
        "ok": error_text is None,
        "output": out_text,
        "error": error_text,
    }