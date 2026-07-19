import streamlit as st
import requests

st.set_page_config(
    page_title="Hospital Login",
    page_icon="🏥"
)

st.title("🏥 Hospital Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login", width="stretch"):

    login_data = {
        "email": email,
        "password": password
    }

    try:
        response = requests.post(
            "https://smart-hospital-backend-sdot.onrender.com",
            json=login_data
        )

        if response.status_code == 200:

           hospital = response.json()["data"]

           st.session_state["logged_in"] = True
           st.session_state["hospital"] = hospital["hospitalName"]
           st.session_state["hospitalId"] = hospital["_id"]
           st.session_state["email"] = hospital["email"]

           st.success("✅ Login Successful!")

        else:
            st.error(response.json()["message"])

    except Exception as e:
        st.error(f"Backend Error: {e}")