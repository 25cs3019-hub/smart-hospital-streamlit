def predict_triage(age, oxygen, heart_rate, systolic_bp, symptom):
    """
    Returns:
    (status, score, reasons, actions)
    """

    score = 0
    reasons = []
    actions = []

    # ---------------- Oxygen ----------------
    if oxygen < 90:
        score += 40
        reasons.append("Low Oxygen Saturation")
    elif oxygen < 95:
        score += 20
        reasons.append("Slightly Low Oxygen")

    # ---------------- Heart Rate ----------------
    if heart_rate > 130:
        score += 25
        reasons.append("Very High Heart Rate")
    elif heart_rate > 110:
        score += 10
        reasons.append("High Heart Rate")

    # ---------------- Blood Pressure ----------------
    if systolic_bp < 90:
        score += 25
        reasons.append("Low Blood Pressure")

    # ---------------- Symptom-based Scoring ----------------
    if symptom == "Chest Pain":
        score += 25
        reasons.append("Possible cardiac emergency.")

    elif symptom == "Difficulty Breathing":
        score += 35
        reasons.append("Possible respiratory distress.")

    elif symptom == "Stroke Symptoms":
        score += 40
        reasons.append("Possible stroke symptoms.")

    elif symptom == "Severe Bleeding":
        score += 40
        reasons.append("Risk of severe blood loss.")

    elif symptom == "Accident":
        score += 20
        reasons.append("Trauma patient.")

    elif symptom == "High Fever":
        score += 10
        reasons.append("Possible infection.")

    # ---------------- Decide Severity ----------------
    if score >= 60:
        status = "🔴 Critical"
        actions = [
            "🚑 Dispatch Ambulance",
            "🫁 Start Oxygen Support",
            "🏥 Admit to ICU Immediately",
            "📞 Alert Emergency Team"
        ]

    elif score >= 30:
        status = "🟡 Moderate"
        actions = [
            "👨‍⚕️ Doctor Consultation",
            "💊 Monitor Patient",
            "🩺 Repeat Vital Check"
        ]

    else:
        status = "🟢 Stable"
        actions = [
            "🏠 Home Care",
            "💧 Stay Hydrated",
            "📅 Follow-up if symptoms worsen"
        ]

    return status, score, reasons, actions