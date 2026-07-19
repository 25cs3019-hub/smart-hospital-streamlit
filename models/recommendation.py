import requests

def recommend_hospital(city="Lucknow"):
    try:
        response = requests.post(
            "https://smart-hospital-backend-sdot.onrender.com",
            json={"city": city}
        )

        if response.status_code == 200:
            hospital = response.json()["data"][0]

            return {
                "Hospital": hospital["hospitalName"],
                "City": hospital["city"],
                "Beds": hospital["availableBeds"],
                "Ventilators": hospital["ventilators"],
                "Score": hospital["availableBeds"] * 2 + hospital["ventilators"]
            }

        return {
            "Hospital": "No Hospital Found",
            "City": "-",
            "Beds": 0,
            "Ventilators": 0,
            "Score": 0
        }

    except Exception:
        return {
            "Hospital": "Backend Offline",
            "City": "-",
            "Beds": 0,
            "Ventilators": 0,
            "Score": 0
        }