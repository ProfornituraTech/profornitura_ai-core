app_name = "profornitura_ai"
app_title = "Profornitura AI"
app_publisher = "Profornitura Italia SRL"
app_description = "Profornitura AI – ERPNext + AI Automation per gare d'appalto (Gare, ANAC, TimelineAI, AutoDecisionAI, DocAI, Logging, Cleanup)."
app_email = "vittorio.erp.ai@gmail.com"
app_license = "MIT"

fixtures = [
    "Custom Field",
    "Property Setter",
    "Custom DocPerm",
    "Workspace",
    "Report",
    "Workflow",
]

# scheduler per TimelineAI
scheduler_events = {
    "daily": [
        "profornitura_ai.timeline.check_upcoming_deadlines.check_upcoming_deadlines"
    ]
}

doc_events = {
    "Gara": {
        "on_update": "profornitura_ai.logs.log_operations.log_gara_update",
        "validate": [
            "profornitura_ai.anac.validate_gara.validate_cig",
            "profornitura_ai.anac.validate_gara.validate_cpv"
        ]
    }
}
