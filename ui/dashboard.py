import streamlit as st

def show_dashboard(data):
    st.subheader(
        "What this exposure could mean"
    )

    left, right = st.columns(2)

    with left:
        st.markdown("### Possible attack paths")

        for path in data.get(
            "attack_paths", []
        ):
            st.markdown(
                f"**{path['title']}**"
            )
            st.write(path["description"])

    with right:
        st.markdown("### Your protection plan")

        for tip in data.get(
            "recommendations", []
        ):
            st.markdown(f"- {tip}")

    st.divider()
    st.subheader("Exposure by data type")

    counts = {}

    for breach in data.get("breaches", []):
        for item in breach.get(
            "data_classes", []
        ):
            counts[item] = (
                counts.get(item, 0) + 1
            )

    if counts:
        st.bar_chart(counts)
    else:
        st.write(
            "No exposed data categories to display."
        )

    st.caption(
        "Risk score is an illustrative project heuristic, "
        "not a validated probability of attack."
    )