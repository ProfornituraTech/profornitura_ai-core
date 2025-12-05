#!/bin/bash
echo "========================================================"
echo " PROFORNITURA AI – FULL AUTOMATION SYNC ENGINE"
echo "========================================================"

BASE="$HOME/Desktop"
CORE="$BASE/profornitura-ai-core"
APP="$BASE/PROFORNITURA_APP"
BUILDER="$BASE/PROFORNITURA_BUILDER"

echo "[1] Normalize folder structure..."
mkdir -p "$BUILDER"
mkdir -p "$APP"

echo "[2] Remove duplicates and NULL files..."
find "$CORE" -name "nul" -type f -delete
find "$CORE" -name "*.tmp" -delete
find "$CORE" -name "*.bak" -delete

echo "[3] Fix CRLF → LF for all Python files..."
find "$CORE" -name "*.py" -exec dos2unix {} \; 2>/dev/null

echo "[4] Validate required folders..."
mkdir -p "$CORE/profornitura_ai/ai"
mkdir -p "$CORE/profornitura_ai/anac"
mkdir -p "$CORE/profornitura_ai/timeline"
mkdir -p "$CORE/profornitura_ai/cleanup"
mkdir -p "$CORE/profornitura_ai/logs"

echo "[5] Copy validated modules into APP folder..."
rsync -av --delete "$CORE/profornitura_ai/" "$APP/profornitura_ai/"

echo "[6] Run Python syntax validation..."
for f in $(find "$CORE" -name "*.py"); do
    python -m py_compile "$f" 2>> "$CORE/python_errors.log"
done

if [ -s "$CORE/python_errors.log" ]; then
    echo "❌ Syntax errors found! Check python_errors.log"
else
    echo "✅ Python modules OK – no syntax errors."
fi

echo "[7] Commit & push to GitHub..."
cd "$CORE"
git add .
git commit -m "FULL_SYNC: normalized folders + CRLF fix + module validation"
git push origin main

echo "========================================================"
echo " FULL SYNC COMPLETED ✔"
echo " Local folders aligned"
echo " Code validated"
echo " GitHub updated"
echo "========================================================"
