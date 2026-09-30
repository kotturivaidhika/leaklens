import streamlit as st

def show_landing():
    st.subheader("Check your digital exposure")

    st.write(
        "Check whether your email appears "
        "in known data breaches."
    )

    with st.container(border=True):
        st.toggle(
            "Demo mode (synthetic sample data)",
            value=True,
            key="demo_mode"
        )

        email = st.text_input(
            "Email address",
            placeholder="you@example.com"
        )

        scan = st.button(
            "🔎 Scan my email",
            type="primary",
            use_container_width=True
        )

    if st.session_state.get("demo_mode", True):
        st.warning(
            "DEMO MODE: Results are synthetic "
            "and are not real breach findings."
        )
    else:
        st.info(
            "LIVE MODE: Requires a valid HIBP API key."
        )

    st.caption(
        "Do not enter passwords, OTPs, or banking details."
    )

    return email, scan