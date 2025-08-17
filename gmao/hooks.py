# -*- coding: utf-8 -*-
from pathlib import Path

app_name = "gmao"
app_title = "Gmao"
app_publisher = "Amine"
app_description = "Application de maintenance"
app_icon = "octicon octicon-tools"
app_color = "blue"
app_email = "amine.hammoud51@gmail.com"
app_license = "MIT"

# 🔹 Assets front-end (inclus seulement si les fichiers existent)
css_path = Path(__file__).parent / "public/css/gmao.css"
js_path = Path(__file__).parent / "public/js/gmao.js"

app_include_css = f"/assets/gmao/css/gmao.css" if css_path.exists() else None
app_include_js = f"/assets/gmao/js/gmao.js" if js_path.exists() else None
