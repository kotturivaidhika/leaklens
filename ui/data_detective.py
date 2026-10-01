from pathlib import Path

import streamlit.components.v1 as components


def show_data_detective():
    html = Path(__file__).with_name(
        "data_detective.html"
    ).read_text(encoding="utf-8")
    components.html(html, height=1100, scrolling=True)