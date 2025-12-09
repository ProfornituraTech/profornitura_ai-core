import frappe

TARGET_APP = "profornitura_ai"
MODULE_NAME = "Profornitura AI"

EXPECTED_DOCTYPES = [
    "Gara",
    "Gara Log Operazioni",
    "Timeline Gara Evento",
    "DocAI Report",
    "DecisionAI Log",
    "AI Request Log",
    "ANAC Regola CIG-CPV",
    "API Log",
    "Gara Form Viewer",
]

def _header(title: str) -> str:
    return f"\n=== {title} ===\n"

def install_check() -> str:
    out = []
    out.append(_header("INSTALL CHECK"))

    out.append(f"Sito: {frappe.local.site}")
    apps = frappe.get_installed_apps()
    out.append(f"App installate: {apps}")

    if TARGET_APP in apps:
        out.append(f"✅ App '{TARGET_APP}' installata.")
    else:
        out.append(f"❌ App '{TARGET_APP}' NON risulta installata su questo sito.")

    return "\n".join(str(x) for x in out)

def module_check() -> str:
    out = []
    out.append(_header("MODULE CHECK"))

    exists = frappe.db.exists("Module Def", MODULE_NAME)
    if exists:
        out.append(f"✅ Module Def '{MODULE_NAME}' presente.")
    else:
        out.append(f"⚠️ Module Def '{MODULE_NAME}' NON trovato.")

    return "\n".join(str(x) for x in out)

def doctype_check() -> str:
    out = []
    out.append(_header("DOCTYPE CHECK"))

    present = []
    missing = []

    for dt in EXPECTED_DOCTYPES:
        if frappe.db.exists("DocType", dt):
            present.append(dt)
            out.append(f"✅ {dt}")
        else:
            missing.append(dt)
            out.append(f"⚠️ {dt} — MANCANTE")

    out.append("\nRiepilogo:")
    out.append(f"Presenti: {present if present else 'nessuno'}")
    out.append(f"Mancanti: {missing if missing else 'nessuno'}")

    return "\n".join(str(x) for x in out)

def full_check() -> str:
    out = []
    out.append(install_check())
    out.append(module_check())
    out.append(doctype_check())
    return "\n".join(out)