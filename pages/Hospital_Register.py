import streamlit as st
import requests

st.set_page_config(
    page_title="Hospital Registration",
    page_icon="🏥"
)

st.title("🏥 Hospital Registration")

hospital = st.text_input("Hospital Name")
city = st.text_input("City")
address = st.text_area("Hospital Address")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
license_no = st.text_input("Hospital License Number")
phone = st.text_input("Emergency Contact Number")

if st.button("Register Hospital", use_container_width=True):

    hospital_data = {
        "hospitalName": hospital,
        "email": email,
        "password": password,
        "phone": phone,
        "address": address,
        "city": city
    }

    try:
        response = requests.post(
            "http://localhost:5000/api/hospitals/register",
            json=hospital_data
        )

        if response.status_code == 201:
            st.success("✅ Hospital Registered Successfully!")

        else:
            st.error(response.json().get("message", "Registration Failed"))

    except Exception as e:
        st.error(f"Backend Error: {e}")