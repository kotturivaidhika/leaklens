from pathlib import Path

import streamlit.components.v1 as components


def show_privacy_tracker():
    html_path = Path(__file__).with_name("data-exposure-checker.html")
    html = html_path.read_text(encoding="utf-8")
    components.html(html, height=1800, scrolling=True)