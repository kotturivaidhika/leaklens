import streamlit as st

def show_results(data):
    breaches = data.get("breaches", [])

    st.subheader("Exposure report")

    mode = data.get("mode", "Unknown")
    st.caption(
        f"Source: {mode} | Email: {data.get('email')}"
    )

    score = data.get("risk_score", 0)
    level = data.get("risk_level", "LOW")

    a, b, c = st.columns(3)

    a.metric(
        "Exposure risk score",
        f"{score}/100"
    )

    b.metric(
        "Risk level",
        level
    )

    c.metric(
        "Known breaches",
        len(breaches)
    )

    if not breaches:
        st.success(
            "No matching breaches were returned "
            "by this source."
        )
        st.write(
            "This does not guarantee that your data "
            "has never been exposed."
        )

    else:
        st.warning(
            "Exposure found. This does not prove "
            "that your account was accessed."
        )

        for breach in breaches:
            name = breach.get("name", "Unknown")
            date = breach.get("date", "Unknown")

            with st.expander(
                f"{name} · {date}",
                expanded=True
            ):
                classes = breach.get(
                    "data_classes", []
                )

                st.write(
                    "**Exposed data:** "
                    + (
                        ", ".join(classes)
                        if classes
                        else "Not specified"
                    )
                )

    with st.expander("Why this score?"):
        for reason in data.get(
            "risk_reasons", []
        ):
            st.write("• " + reason)