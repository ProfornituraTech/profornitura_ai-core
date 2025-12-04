# ===========================================================
# PROFORNITURA AI - AUTO STRUCTURE BUILDER FOR FRAPPE APP
# Creates all required files for a valid Frappe App (v15)
# CTO: Vittorio Paolella - Profornitura Italia SRL
# ===========================================================

Write-Host "=== PROFORNITURA AI - AUTO STRUCTURE BUILDER ===" -ForegroundColor Cyan

# Detect current folder
$base = Get-Location
Write-Host "Working directory: $base"

# Required folders
$folders = @(
    "profornitura_ai",
    "profornitura_ai/config",
    "profornitura_ai/templates",
    "profornitura_ai/public",
    "profornitura_ai/ai",
    "profornitura_ai/api",
    "profornitura_ai/compliance_anac",
    "profornitura_ai/utils"
)

foreach ($f in $folders) {
    if (-not (Test-Path $f)) {
        New-Item -ItemType Directory -Path $f | Out-Null
        Write-Host "Created folder: $f"
    }
}

# === FILE: __init__.py ======================================
$init = @"
# Profornitura AI - Frappe App
"@
Set-Content -Path "profornitura_ai/__init__.py" -Value $init

# === FILE: hooks.py =========================================
$hooks = @"
app_name = "profornitura_ai"
app_title = "Profornitura AI"
app_publisher = "Profornitura Italia SRL"
app_description = "AI Automation for Public Tenders"
app_email = "vittorio.erp.ai@gmail.com"
app_license = "MIT"

fixtures = [
    {"dt": "Custom Field"},
    {"dt": "Client Script"},
    {"dt": "Server Script"},
    {"dt": "Workflow"},
    {"dt": "Workflow Action Master"},
    {"dt": "Workspace"}
]
"@
Set-Content -Path "profornitura_ai/hooks.py" -Value $hooks

# === FILE: modules.txt =======================================
$modules = @"
Profornitura AI
"@
Set-Content -Path "profornitura_ai/modules.txt" -Value $modules

# === FILE: patches.txt =======================================
$patches = @"
# Patches for Profornitura AI
"@
Set-Content -Path "profornitura_ai/patches.txt" -Value $patches

# === FILE: desktop.py ========================================
$desktop = @"
# Profornitura AI Workspace Icon
"@
Set-Content -Path "profornitura_ai/config/desktop.py" -Value $desktop

# === FILE: MANIFEST.in =======================================
$manifest = @"
include MANIFEST.in
include requirements.txt
recursive-include profornitura_ai *
"@
Set-Content -Path "MANIFEST.in" -Value $manifest

# === FILE: setup.py ==========================================
$setup = @"
from setuptools import setup, find_packages

setup(
    name="profornitura_ai",
    version="1.0.0",
    description="Profornitura AI – ERPNext Automation App",
    author="Profornitura Italia SRL",
    author_email="vittorio.erp.ai@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
"@
Set-Content -Path "setup.py" -Value $setup

# === FILE: requirements.txt ==================================
$req = @"
frappe
erpnext
"@
Set-Content -Path "requirements.txt" -Value $req

Write-Host "=============================================="
Write-Host "  ✔ STRUCTURE COMPLETED SUCCESSFULLY"
Write-Host "  ✔ Your app is now a VALID Frappe App"
Write-Host "=============================================="
Write-Host "Next steps:"
Write-Host "1) git add ."
Write-Host "2) git commit -m 'App Structure Completed'"
Write-Host "3) git push"
