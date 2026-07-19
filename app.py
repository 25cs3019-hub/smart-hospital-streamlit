import streamlit as st

# ------------------ Page Configuration ------------------
st.set_page_config(
    page_title="Smart Hospital Resource Network",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------ Custom CSS ------------------
st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

h1 {
    color: #d32f2f;
    text-align: center;
}

.stButton > button {
    width: 100%;
    border-radius: 10px;
    background-color: #d32f2f;
    color: white;
    font-weight: bold;
}

.stMetric {
    background-color: #ffffff;
    padding: 10px;
    border-radius: 10px;
    border: 1px solid #eeeeee;
}

</style>
""", unsafe_allow_html=True)

# ------------------ Sidebar ------------------
with st.sidebar:
    st.title("🏥 Smart Hospital")
    st.success("Emergency Response System")
    st.markdown("---")
    st.info("Use the sidebar to navigate through the application.")

# ------------------ Main Page ------------------
st.title("🏥 Smart Hospital Resource Network")

st.markdown("""
## Welcome 👋

This prototype helps hospitals and emergency responders manage resources efficiently.

### 🚀 Features

- 🚑 AI Emergency Triage
- 🏥 Hospital Dashboard
- 🩸 Blood Bank Availability
- 🚑 Ambulance Tracking
- 📈 ICU Bed Prediction
- 🗺️ Nearby Hospital Map
- ⚙️ Admin Panel
- 🤖 Smart Hospital Recommendation

---
""")

st.success("✅ Project is running successfully!")

st.info("Select any page from the left sidebar to start using the application.")