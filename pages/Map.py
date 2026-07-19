import streamlit as st
import requests
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Hospital Map",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ Smart Hospital Resource Map")

# Demo coordinates for cities
coordinates = {
    "Lucknow": (26.8467, 80.9462),
    "Delhi": (28.6139, 77.2090),
    "Kanpur": (26.4499, 80.3319),
    "Noida": (28.5355, 77.3910),
    "Varanasi": (25.3176, 82.9739),
    "Prayagraj": (25.4358, 81.8463),
}

try:
    response = requests.get("https://smart-hospital-backend-sdot.onrender.com/api/hospitals")

    if response.status_code == 200:

        result = response.json()

        hospitals = result["data"]
        
        for hospital in hospitals:
          if "availableBeds" not in hospital:
            hospital["availableBeds"] = hospital.get("generalBeds", 0)

          if "icuBeds" not in hospital:
            hospital["icuBeds"] = 0

          if "ventilators" not in hospital:
           hospital["ventilators"] = 0

        m = folium.Map(
            location=[26.8467, 80.9462],
            zoom_start=7
        )

        for hospital in hospitals:

            city = hospital["city"]

            lat, lon = coordinates.get(
                city,
                (26.8467, 80.9462)
            )

            beds = hospital["availableBeds"]

            if beds > 10:
                marker_color = "green"
            elif beds > 0:
                marker_color = "orange"
            else:
                marker_color = "red"

            popup = f"""
<b>{hospital['hospitalName']}</b><br>
📍 {hospital['address']}<br>
City : {hospital['city']}<br>
Available Beds : {hospital['availableBeds']}<br>
ICU Beds : {hospital['icuBeds']}<br>
Ventilators : {hospital['ventilators']}<br>
Blood Bank : {'Yes' if hospital['bloodBankAvailable'] else 'No'}<br>
Ambulance : {'Yes' if hospital['ambulanceAvailable'] else 'No'}
"""

            folium.Marker(
                location=[lat, lon],
                popup=folium.Popup(popup, max_width=300),
                tooltip=hospital["hospitalName"],
                icon=folium.Icon(
                    color=marker_color,
                    icon="plus"
                )
            ).add_to(m)

        st_folium(
            m,
            width=1200,
            height=650
        )

    else:
        st.error(f"Backend returned status {response.status_code}")

except Exception as e:
    st.error(f"Error: {e}")

st.markdown("---")
st.caption("© 2026 Smart Hospital Resource Network | Hackathon Prototype")