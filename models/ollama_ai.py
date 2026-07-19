import ollama

MODEL = "gemma3:4b"

def get_ai_response(patient, result, score):

    prompt = f"""
You are an emergency triage assistant.

Risk Level:
{result}

Risk Score:
{score}/100

Patient Details:
Age: {patient['age']}
Gender: {patient['gender']}
Symptom: {patient['symptom']}
Oxygen: {patient['oxygen']}%
Heart Rate: {patient['heart_rate']}
Blood Pressure: {patient['bp']}
Temperature: {patient['temperature']}
Respiratory Rate: {patient['respiratory_rate']}

Explain:
1. Why this risk level was assigned.
2. Immediate first aid.
3. Hospital advice.

Keep the answer under 120 words.
"""

    try:

        response = ollama.chat(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception:

        return """
### AI Summary

• Patient analysis completed successfully.

• Please follow the recommended emergency actions.

• Visit the recommended hospital immediately if the patient is Critical.

• This response is generated because the local AI server is currently unavailable.
"""