import streamlit as st

st.title("🏥 Smart Hospital Resource Network")

st.markdown("""
## AI-Powered Emergency Resource Management

Helping patients find:

- 🚑 Emergency Triage
- 🏥 ICU Beds
- 🩸 Blood Banks
- 🚑 Ambulances
- 📈 ICU Prediction

---
""")

col1, col2, col3 = st.columns(3)

col1.metric("Hospitals", "10")
col2.metric("Blood Banks", "5")
col3.metric("Ambulances", "7")

st.success("Ready for emergency response.")
st.markdown("---")
st.caption("© 2026 Smart Hospital Resource Network | Built for Hackathon")