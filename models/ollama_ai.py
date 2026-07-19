def get_ai_response(patient, result, score):
    return f"""
### 🤖 AI Medical Assistant

**Risk Level:** {result}

**Risk Score:** {score}/100

**Patient Summary**

- Age: {patient['age']}
- Symptom: {patient['symptom']}
- Oxygen: {patient['oxygen']}%
- Heart Rate: {patient['heart_rate']}

### Recommendation

The patient should be evaluated by a qualified medical professional as soon as possible.

Follow the emergency actions shown above and transport the patient to the recommended hospital if required.
"""