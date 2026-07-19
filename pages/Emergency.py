import streamlit as st
import time
import requests

from models.triage import predict_triage
from models.ollama_ai import get_ai_response
from models.report import create_report

st.set_page_config(
    page_title="AI Emergency Triage",
    page_icon="🚑",
    layout="wide"
)

st.title("🚑 Smart Hospital Resource Network")
st.warning("⚠️ Prototype for Hackathon Demonstration")

# ---------------------------------------------------
# Patient Information
# ---------------------------------------------------

st.subheader("👤 Patient Information")

col1, col2 = st.columns(2)

with col1:
    patient_name = st.text_input("Patient Name")
    age = st.number_input(
        "Age",
        min_value=0,
        max_value=120,
        value=30
    )

    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female",
            "Other"
        ]
    )

with col2:

    symptom = st.selectbox(
        "Primary Symptom",
        [
            "Chest Pain",
            "Difficulty Breathing",
            "Stroke Symptoms",
            "Severe Bleeding",
            "Accident",
            "High Fever",
            "Other"
        ]
    )

    pain = st.slider(
        "Pain Severity",
        1,
        10,
        5
    )

# ---------------------------------------------------
# Vital Signs
# ---------------------------------------------------

st.subheader("🩺 Vital Signs")

c1, c2 = st.columns(2)

with c1:

    oxygen = st.slider(
        "Oxygen Saturation (%)",
        50,
        100,
        98
    )

    heart_rate = st.slider(
        "Heart Rate (BPM)",
        40,
        180,
        80
    )

    respiratory_rate = st.slider(
        "Respiratory Rate",
        10,
        40,
        18
    )

with c2:

    systolic_bp = st.slider(
        "Systolic Blood Pressure",
        50,
        200,
        120
    )

    temperature = st.slider(
        "Temperature (°C)",
        35.0,
        42.0,
        37.0
    )

st.divider()

# ---------------------------------------------------
# Analyze Button
# ---------------------------------------------------

if st.button("🔍 Analyze Patient", width="stretch"):

    with st.spinner("Analyzing Patient..."):
        time.sleep(2)

    result, score, reasons, actions = predict_triage(
        age,
        oxygen,
        heart_rate,
        systolic_bp,
        symptom
    )

    st.subheader("🤖 AI Assessment")

    st.metric(
        "Risk Score",
        f"{score}/100"
    )

    if "Critical" in result:
        st.error(result)

    elif "Moderate" in result:
        st.warning(result)

    else:
        st.success(result)

    st.subheader("📋 Reasons")

    if reasons:
        for reason in reasons:
            st.write("•", reason)
    else:
        st.write("No major risk factors detected.")

    st.subheader("🚑 Recommended Actions")

    for action in actions:
        st.write(action)
    
# ---------------------------------------------------
# Hospital Recommendation
# ---------------------------------------------------

try:
    response = requests.post(
        "https://smart-hospital-backend-sdot.onrender.com/api/recommend",
        json={"city": "Lucknow"}
    )

    if response.status_code == 200:
        result_data = response.json()

        if result_data.get("data"):
            hospital = result_data["data"][0]
        else:
            hospital = {
                "hospitalName": "No Hospital Found",
                "city": "-",
                "availableBeds": 0,
                "ventilators": 0
            }

    else:
        hospital = {
            "hospitalName": "No Hospital Found",
            "city": "-",
            "availableBeds": 0,
            "ventilators": 0
        }

except Exception:
    hospital = {
        "hospitalName": "Backend Offline",
        "city": "-",
        "availableBeds": 0,
        "ventilators": 0
    }

st.divider()

st.subheader("🏥 Recommended Hospital")

st.success(f"""
### 🏥 {hospital['hospitalName']}

📍 **City:** {hospital['city']}

🛏️ **Available Beds:** {hospital.get('availableBeds', 0)}

🫁 **Ventilators:** {hospital.get('ventilators', 0)}
""")

# ---------------------------------------------------
# Patient Dictionary
# ---------------------------------------------------

patient = {
    "name": patient_name,
    "age": age,
    "gender": gender,
    "symptom": symptom,
    "pain": pain,
    "oxygen": oxygen,
    "heart_rate": heart_rate,
    "bp": systolic_bp,
    "temperature": temperature,
    "respiratory_rate": respiratory_rate,
}

# ---------------------------------------------------
# AI Medical Assistant
# ---------------------------------------------------

st.divider()

st.subheader("🧠 AI Medical Assistant (Gemma 3)")

with st.spinner("Consulting AI..."):
    try:
        ai_response = get_ai_response(
            patient,
            result,
            score
        )

        st.markdown(ai_response)

    except Exception:

        ai_response = (
            "⚠️ Local AI is currently unavailable.\n\n"
            "Patient has been analyzed successfully using the triage engine.\n"
            "Please review the recommended hospital and emergency actions."
        )

        st.warning(ai_response)

# ---------------------------------------------------
# Generate Emergency PDF Report
# ---------------------------------------------------

st.divider()

try:

    pdf_file = create_report(
        patient,
        result,
        score,
        hospital,
        ai_response
    )

    st.success("✅ Emergency report generated successfully!")

    with open(pdf_file, "rb") as file:

        st.download_button(
            label="📄 Download Emergency Report",
            data=file,
            file_name="Emergency_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )

except Exception as e:

    st.error(f"PDF Generation Error: {e}")

# ---------------------------------------------------
# Disclaimer
# ---------------------------------------------------

st.divider()

st.info("""
### 📢 Disclaimer

The AI recommendations are generated for demonstration purposes only.

Always consult qualified medical professionals during a real emergency.
""")