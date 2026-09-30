import streamlit as st

from ui.landing import show_landing
from ui.results import show_results
from ui.dashboard import show_dashboard

from backend.hibp_api import check_email
from security.risk_engine import calculate_risk
from security.attack_paths import get_attack_paths
from security.recommendations import get_recommendations

st.set_page_config(
    page_title="LeakLens",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ LeakLens")
st.caption(
    "Discover your exposed data. "
    "Understand the risk. Take action."
)

email, scan = show_landing()

if scan:
    st.session_state.pop("scan_result", None)

    if (
        not email
        or "@" not in email
        or "." not in email.split("@")[-1]
    ):
        st.error("Enter a valid email address.")

    else:
        try:
            with st.spinner("Scanning..."):
                data = check_email(email.strip())

                score, level, reasons = (
                    calculate_risk(data)
                )

                data["risk_score"] = score
                data["risk_level"] = level
                data["risk_reasons"] = reasons

                data["attack_paths"] = (
                    get_attack_paths(data)
                )

                data["recommendations"] = (
                    get_recommendations(data)
                )

                st.session_state[
                    "scan_result"
                ] = data

        except Exception as e:
            st.error(str(e))

result = st.session_state.get("scan_result")

if result:
    st.divider()
    show_results(result)
    show_dashboard(result)
else:
    st.info(
        "Enter an email and click Scan my email "
        "to begin."
    )