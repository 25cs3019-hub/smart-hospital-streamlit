import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="🛠️",
    layout="wide"
)

st.title("🛠️ Smart Hospital Admin Dashboard")

try:
    
    response = requests.get("https://smart-hospital-backend-sdot.onrender.com/api/hospitals")
    if response.status_code == 200:

        result = response.json()
        hospitals = result["data"]

        st.success(f"Total Registered Hospitals: {len(hospitals)}")

        if hospitals:

            df = pd.DataFrame(hospitals)
            if "availableBeds" not in df.columns:
             df["availableBeds"] = df["generalBeds"] if "generalBeds" in df.columns else 0

            if "icuBeds" not in df.columns:
             df["icuBeds"] = 0

            if "ventilators" not in df.columns:
             df["ventilators"] = 0

            show = df[[
                "hospitalName",
                "city",
                "icuBeds",
                "availableBeds",
                "ventilators",
                "bloodBankAvailable",
                "ambulanceAvailable"
            ]]

            st.dataframe(show, use_container_width=True)

            st.subheader("Hospital Statistics")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Hospitals",
                    len(df)
                )

            with col2:
                st.metric(
                    "Total ICU Beds",
                    int(df["icuBeds"].sum())
                )

            with col3:
                st.metric(
                    "Available Beds",
                    int(df["availableBeds"].sum())
                )

        else:
            st.warning("No hospitals registered.")

    else:
        st.error("Could not fetch hospitals.")

except Exception as e:
    st.error(e)

st.markdown("---")
st.caption("© 2026 Smart Hospital Resource Network")