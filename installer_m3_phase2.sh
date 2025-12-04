#!/bin/bash
echo "========================================================="
echo "        PROFORNITURA AI – M3 PHASE 2 AUTO INSTALLER      "
echo "========================================================="

# --- CONFIG ------------------------------------------------
APP_NAME="profornitura_ai"
SITE_STAGING="profornitura-ai-core.frappe.cloud"
REPORT_DIR="M3_PHASE2_DEPLOY_REPORT"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

mkdir -p "$REPORT_DIR"

echo "[1/9] 🔄 Pull ultimi aggiornamenti da GitHub..."
git pull origin main &>> "$REPORT_DIR/git_pull_$TIMESTAMP.log"

echo "[2/9] 📦 Scarico app su Frappe Cloud (staging)..."
bench get-app https://github.com/ProfornituraTech/profornitura_ai-core.git \
    --branch main &>> "$REPORT_DIR/get_app_$TIMESTAMP.log"

echo "[3/9] 🏗 Installo app sul sito..."
bench --site $SITE_STAGING install-app $APP_NAME \
    &>> "$REPORT_DIR/install_app_$TIMESTAMP.log"

echo "[4/9] 📁 Carico fixtures (doctype, fields, workflow)..."
bench --site $SITE_STAGING migrate &>> "$REPORT_DIR/migrate_$TIMESTAMP.log"

echo "[5/9] ⚙️ Applico Workflow e ANAC Validator..."
bench --site $SITE_STAGING execute $APP_NAME.scripts.apply_workflows \
    &>> "$REPORT_DIR/workflow_$TIMESTAMP.log"

bench --site $SITE_STAGING execute $APP_NAME.scripts.load_anac_rules \
    &>> "$REPORT_DIR/anac_rules_$TIMESTAMP.log"

echo "[6/9] ⏱ Attivo schedulers per TimelineAI + Audit..."
bench --site $SITE_STAGING set-config enable_scheduler 1
bench --site $SITE_STAGING scheduler enable &>> "$REPORT_DIR/scheduler_$TIMESTAMP.log"

echo "[7/9] 🔍 Test diagnostici..."
bench --site $SITE_STAGING doctor &>> "$REPORT_DIR/doctor_$TIMESTAMP.log"
bench --site $SITE_STAGING list-apps &>> "$REPORT_DIR/apps_list_$TIMESTAMP.log"

echo "[8/9] 🧪 Test funzione TimelineAI..."
bench --site $SITE_STAGING execute $APP_NAME.timeline.check_deadlines \
    &>> "$REPORT_DIR/timeline_test_$TIMESTAMP.log"

echo "[9/9] 📦 Compilo report ZIP..."
zip -r M3_PHASE2_DEPLOY_REPORT_$TIMESTAMP.zip "$REPORT_DIR" \
    &>> "$REPORT_DIR/zip_$TIMESTAMP.log"

echo "========================================================="
echo " ✅ INSTALLER COMPLETATO!"
echo " 🔍 FILE REPORT GENERATO: M3_PHASE2_DEPLOY_REPORT_$TIMESTAMP.zip"
echo "========================================================="
