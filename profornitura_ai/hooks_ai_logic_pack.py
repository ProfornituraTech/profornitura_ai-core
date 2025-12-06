# Frammento di hooks per SUPER_SUITE_AI_LOGIC_PACK v2 ENTERPRISE

AI_DOC_EVENTS = {
    "Gara": {
        "on_update": "profornitura_ai.profornitura_ai.ai.autopilot.autopilot_engine.run_gara_autopilot",
        "after_insert": "profornitura_ai.profornitura_ai.ai.autopilot.autopilot_engine.run_gara_autopilot",
    }
}

AI_SCHEDULER_EVENTS = {
    "daily": [
        "profornitura_ai.profornitura_ai.ai.autopilot.autopilot_engine.run_gara_autopilot"
    ]
}
