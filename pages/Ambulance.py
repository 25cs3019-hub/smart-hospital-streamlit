import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🚑 Ambulance Tracking")

df = pd.read_csv("data/ambulances.csv")

status = st.selectbox(
    "Filter by Status",
    ["All", "Available", "On Duty"]
)

if status != "All":
    df = df[df["Status"] == status]

st.dataframe(df, use_container_width=True)

available = len(df[df["Status"] == "Available"])

st.success(f"🚑 {available} Ambulances Available")

fig = px.pie(
    df,
    names="Status",
    title="Ambulance Status"
)

st.plotly_chart(fig, use_container_width=True)
st.markdown("---")
st.caption("© 2026 Smart Hospital Resource Network | Built for Hackathon")