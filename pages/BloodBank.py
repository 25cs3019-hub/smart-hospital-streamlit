import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🩸 Blood Bank Availability")

df = pd.read_csv("data/bloodbanks.csv")

blood_group = st.selectbox(
    "Select Blood Group",
    sorted(df["BloodGroup"].unique())
)

filtered = df[df["BloodGroup"] == blood_group]

st.subheader(f"Available {blood_group} Blood")

if filtered.empty:
    st.error("No blood units available.")
else:
    st.dataframe(filtered, use_container_width=True)

    total_units = filtered["Units"].sum()

    st.success(f"🩸 Total Available Units: {total_units}")

    fig = px.bar(
        filtered,
        x="BloodBank",
        y="Units",
        color="City",
        title=f"{blood_group} Blood Availability"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.markdown("---")
st.caption("© 2026 Smart Hospital Resource Network | Built for Hackathon")