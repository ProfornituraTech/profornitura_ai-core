🟦 PROFORNITURA AI — ENTERPRISE EDITION
ERPNext + AI Automation Platform for Italian Public Tenders

Developed by Profornitura Italia SRL

📌 Overview

Profornitura AI è una piattaforma enterprise costruita su ERPNext v15 + Frappe Framework, progettata per automatizzare completamente il ciclo di vita delle gare d’appalto italiane:

Consip

Sintel

MEPA

ANAC

TED Europa

La piattaforma integra moduli AI proprietari:

DocAI – Parsing documentale avanzato (PDF bando, capitolato)

DecisionAI – Verifica di idoneità e scoring automatico

TimelineAI – Generazione eventi di gara, reminder, scadenze

ANAC Layer – Validazione CIG & CPV

Cleanup & Log Management

Tutti i moduli sono stati estratti direttamente da un ambiente ERPNext reale tramite l’Enterprise Builder v1.0.

📁 Directory Structure
profornitura_ai/
│
├── ai/
│   ├── doc_ai_engine.py
│   ├── decision_ai_engine.py
│   └── __init__.py
│
├── anac/
│   ├── validate_gara.py
│   └── __init__.py
│
├── timeline/
│   ├── check_upcoming_deadlines.py
│   └── __init__.py
│
├── logs/
│   ├── log_operations.py
│   └── __init__.py
│
├── cleanup/
│   ├── auto_cleanup.py
│   └── __init__.py
│
├── fixtures/
│   ├── doctypes_meta.json
│   ├── doctypes_data.json
│   ├── workflows.json
│   ├── custom_fields.json
│   ├── custom_perms.json
│   ├── property_setters.json
│   ├── workspaces.json
│   ├── reports.json
│   └── ...
│
├── hooks.py
├── modules.txt
├── setup.py
└── __init__.py

⚙️ Installation (Bench)
bench get-app https://github.com/profornituratech/profornitura_ai-core.git
bench --site [sitename] install-app profornitura_ai
bench migrate
bench clear-cache

⚙️ Installation (Frappe Cloud)

Vai su Sites → App Store → Install from GitHub

Inserisci URL:

https://github.com/profornituratech/profornitura_ai-core.git


Installa l’app sul sito desiderato

Esegui:

bench migrate

bench restart

📌 Features incluse in questa versione (v1.0.0)
🔹 15 Doctype Enterprise

Gara, Offerta, DocAI Report, DecisionAI Log, Timeline Event, ANAC Rule, ecc.

🔹 Workflow di Gara

Bozza

In Valutazione

Idonea / Non Idonea

Offerta Inviata

Aggiudicata

Annullata

🔹 AI Modules

DocAI: parsing PDF con estrazione JSON

DecisionAI: calcolo automatico idoneità SRL nuova

TimelineAI: reminder scadenze giornalieri

ANAC Validator: matching CIG/CPV

🔹 Logging avanzato

Log operazioni gara

Log API

Log AI

🔹 Fixtures complete

Pronte per deployment enterprise uniforme.

🔒 Security Model

L’app include:

ROLE: CTO, Bid Manager, Compliance Officer, Vendor Developer

Hardening dei permessi

Audit Trail integrato

🧱 Future Roadmap (M3-M4)

Integrazione API (Consip/Sintel/Mepa/TED)

AI Parsing avanzato multi-file

Dashboard Strategica

API Marketplace

📌 End of README.md
