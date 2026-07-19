import streamlit as st
import requests

st.set_page_config(
    page_title="Hospital Panel",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Hospital Resource Dashboard")

if "logged_in" not in st.session_state:
    st.error("Please login first.")
    st.stop()

hospital_id = st.session_state["hospitalId"]

st.info(f"Hospital ID: {hospital_id}")

try:
    response = requests.get(
        f"https://smart-hospital-backend-sdot.onrender.com/{hospital_id}"
    )

    if response.status_code != 200:
        st.error("Unable to fetch hospital data")
        st.stop()

    hospital = response.json()["data"]

except Exception as e:
    st.error(f"Backend Error: {e}")
    st.stop()

st.subheader(hospital["hospitalName"])

col1, col2 = st.columns(2)

with col1:
    generalBeds = st.number_input(
        "General Beds",
        min_value=0,
        value=int(hospital.get("generalBeds", 0))
    )

    availableBeds = st.number_input(
        "Available Beds",
        min_value=0,
        value=int(hospital.get("availableBeds", 0))
    )

    icuBeds = st.number_input(
        "ICU Beds",
        min_value=0,
        value=int(hospital.get("icuBeds", 0))
    )

with col2:
    ventilators = st.number_input(
        "Ventilators",
        min_value=0,
        value=int(hospital.get("ventilators", 0))
    )

    oxygen = st.number_input(
        "Oxygen Cylinders",
        min_value=0,
        value=int(hospital.get("oxygenCylinders", 0))
    )

blood = st.checkbox(
    "Blood Bank Available",
    value=hospital.get("bloodBankAvailable", False)
)

ambulance = st.checkbox(
    "Ambulance Available",
    value=hospital.get("ambulanceAvailable", False)
)

if st.button("💾 Update Resources", use_container_width=True):

    payload = {
        "generalBeds": generalBeds,
        "availableBeds": availableBeds,
        "icuBeds": icuBeds,
        "ventilators": ventilators,
        "oxygenCylinders": oxygen,
        "bloodBankAvailable": blood,
        "ambulanceAvailable": ambulance
    }

    try:
        update = requests.put(
            f"https://smart-hospital-backend-sdot.onrender.com/api/hospitals/{hospital_id}",
            json=payload
        )

        st.write("Status Code:", update.status_code)

        try:
            st.json(update.json())
        except:
            st.write(update.text)

        if update.status_code == 200:
            st.success("✅ Resources Updated Successfully!")
            st.balloons()

        else:
            st.error("Update Failed")

    except Exception as e:
        st.error(e)