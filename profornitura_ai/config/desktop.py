from frappe import _

def get_data():
    return [
        {
            "label": _("Profornitura AI"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Gara",
                    "label": _("Gara"),
                },
                {
                    "type": "doctype",
                    "name": "DocAI Report",
                    "label": _("DocAI Report"),
                },
                {
                    "type": "doctype",
                    "name": "AutoDecisionAI Log",
                    "label": _("AutoDecisionAI Log"),
                },
            ],
        }
    ]
