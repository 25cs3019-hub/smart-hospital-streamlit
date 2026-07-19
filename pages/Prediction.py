import streamlit as st
import pandas as pd
import plotly.express as px

from models.prediction import predict_next_day

st.title("📈 ICU Bed Prediction")

df = pd.read_csv("data/icu_history.csv")

prediction = predict_next_day()

st.metric(
    "Predicted Occupied Beds Tomorrow",
    prediction
)

fig = px.line(
    df,
    x="Day",
    y="OccupiedBeds",
    markers=True,
    title="ICU Occupancy Trend"
)

st.plotly_chart(fig, use_container_width=True)

st.success(
    f"AI predicts approximately {prediction} ICU beds will be occupied tomorrow."
)
st.markdown("---")
st.caption("© 2026 Smart Hospital Resource Network | Built for Hackathon")