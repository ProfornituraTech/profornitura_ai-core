
from __future__ import unicode_literals

app_name = "profornitura_ai"
app_title = "Profornitura AI"
app_publisher = "Profornitura Italia SRL"
app_description = "ERPNext + AI Automation Platform"
app_email = "vittorio.erp.ai@gmail.com"
app_license = "MIT"

doc_events = {
    "Gara": {
        "validate": "profornitura_ai.anac.validate_gara.validate_gara_compliance",
        "after_insert": "profornitura_ai.logs.log_operations.log_gara_insert",
        "on_update": "profornitura_ai.logs.log_operations.log_gara_update",
        "on_cancel": "profornitura_ai.logs.log_operations.log_gara_cancel",
    }
}

scheduler_events = {
    "daily": [
        "profornitura_ai.timeline.check_upcoming_deadlines.send_deadline_reminders"
    ]
}
