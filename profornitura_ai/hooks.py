app_name = "profornitura_ai"
app_title = "Profornitura AI"
app_publisher = "Vittorio Paolella"
app_description = "Automation Suite per gare"
app_email = "vittorio.erp.ai@gmail.com"
app_license = "MIT"
# Importazione automatica di Doctype e configurazioni
fixtures = [
    {"dt": "DocType", "filters": [["module", "=", "Profornitura AI"]]},
    {"dt": "Custom Field"},
    {"dt": "Custom DocPerm"},
    {"dt": "Notification"},
    {"dt": "Workspace"},
    {"dt": "Role"},
    {"dt": "Role Profile"},
    {"dt": "Property Setter"},
    {"dt": "Print Format"},
    {"dt": "Client Script"},
    {"dt": "Server Script"},
    {"dt": "Web Form"}
]
