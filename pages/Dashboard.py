import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

st.title("🏥 Smart Hospital Dashboard")

# Fetch data from backend
try:
    response = requests.get("http://localhost:5000/api/hospitals")

    if response.status_code != 200:
        st.error("Unable to fetch hospitals.")
        st.stop()

    hospitals = response.json()["data"]

except Exception as e:
    st.error(f"Backend Error: {e}")
    st.stop()

if len(hospitals) == 0:
    st.warning("No hospitals registered.")
    st.stop()

df = pd.DataFrame(hospitals)

# Make sure columns exist
for col in [
    "generalBeds",
    "availableBeds",
    "icuBeds",
    "ventilators",
]:
    if col not in df.columns:
        df[col] = 0

# KPIs
totalHospitals = len(df)
generalBeds = df["generalBeds"].sum()
availableBeds = df["availableBeds"].sum()
icuBeds = df["icuBeds"].sum()
ventilators = df["ventilators"].sum()

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("🏥 Hospitals", totalHospitals)
c2.metric("🛏 Beds", generalBeds)
c3.metric("🟢 Available", availableBeds)
c4.metric("❤️ ICU", icuBeds)
c5.metric("🫁 Ventilators", ventilators)

st.divider()

st.subheader("Registered Hospitals")

show = df[
    [
        "hospitalName",
        "city",
        "generalBeds",
        "availableBeds",
        "icuBeds",
        "ventilators",
    ]
]

st.dataframe(show, use_container_width=True)

st.divider()

fig = px.bar(
    df,
    x="hospitalName",
    y="availableBeds",
    color="city",
    title="Available Beds"
)

st.plotly_chart(fig, use_container_width=True)

fig2 = px.pie(
    df,
    names="city",
    values="availableBeds",
    title="Beds Distribution"
)

st.plotly_chart(fig2, use_container_width=True)
st.success("✅ Resources Updated Successfully!")
st.rerun()

if st.button("🔄 Refresh Dashboard"):
    st.rerun()