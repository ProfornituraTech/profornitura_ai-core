#!/bin/bash

echo "==============================================="
echo " PROFORNITURA AI – FULL AUTOMATION SYNC"
echo " PC → GitHub → Frappe Cloud"
echo "==============================================="

APP_DIR="$HOME/Desktop/profornitura-ai-app/profornitura_ai"
CORE_DIR="$HOME/Desktop/profornitura-ai-core"
TMP_SYNC="$HOME/Desktop/profornitura_sync_tmp"

echo "[1] Pulizia cartella temporanea..."
rm -rf "$TMP_SYNC"
mkdir -p "$TMP_SYNC"

echo "[2] Copia dei moduli AI/ANAC/Workflow nell'app ufficiale..."
cp -r "$CORE_DIR/ai" "$APP_DIR/"
cp -r "$CORE_DIR/anac" "$APP_DIR/"
cp -r "$CORE_DIR/timeline" "$APP_DIR/"
cp -r "$CORE_DIR/logs" "$APP_DIR/"
cp -r "$CORE_DIR/cleanup" "$APP_DIR/"

echo "[3] Rimozione caratteri non validi dai file Python..."
find "$APP_DIR" -name "*.py" | while read f; do
  sed -i 's/\\\"/"/g' "$f"
  sed -i 's/\r$//g' "$f"
done

echo "[4] Validazione sintassi Python..."
find "$APP_DIR" -name "*.py" | while read f; do
  python -m py_compile "$f" 2>> "$TMP_SYNC/errors.log"
done

if [ -s "$TMP_SYNC/errors.log" ]; then
  echo "❌ Errori trovati nella sintassi Python!"
  cat "$TMP_SYNC/errors.log"
  exit 1
else
  echo "✓ Nessun errore di sintassi."
fi

echo "[5] Commit & Push dell'app..."
cd "$APP_DIR"
git add .
git commit -m "Full sync + AI + ANAC + cleanup + workflow"
git push origin main

echo "[6] Push del CORE..."
cd "$CORE_DIR"
git add .
git commit -m "Sync CORE + script builder + packs"
git push origin main

echo "==============================================="
echo " COMPLETATO – TUTTO ORDINATO E SINCRONIZZATO"
echo " Ora puoi fare Deploy su Frappe Cloud."
echo "==============================================="
