import streamlit as st
import requests
import os

# Get backend URL from environment variable or default to localhost
BACKEND_URL = os.getenv('BACKEND_URL', 'http://localhost:8000')

def main():
    st.set_page_config(page_title="Insurance Premium Predictor", layout="centered")
    st.title("Insurance Premium Prediction")
    st.markdown("""
    Enter your details below to predict your insurance premium category.
    """)
    with st.form("prediction_form"):
        age = st.number_input("Age", min_value=1, max_value=120, value=30)
        weight = st.number_input("Weight (kg)", min_value=1.0, max_value=200.0, value=70.0)
        height = st.number_input("Height (meters)", min_value=0.5, max_value=2.5, value=1.7)
        income_lpa = st.number_input("Annual Income (LPA)", min_value=1.0, max_value=100.0, value=10.0)
        smoker = st.selectbox("Are you a smoker?", [False, True], format_func=lambda x: "Yes" if x else "No")
        city = st.text_input("City", value="Pune")
        occupation = st.selectbox(
            "Occupation",
            ["retired", "freelancer", "student", "government_job", "business_owner", "unemployed", "private_job"]
        )
        submit = st.form_submit_button("Predict Premium")
    if submit:
        user_data = {
            "age": age,
            "weight": weight,
            "height": height,
            "income_lpa": income_lpa,
            "smoker": smoker,
            "city": city,
            "occupation": occupation
        }
        try:
            response = requests.post(f"{BACKEND_URL}/predict", json=user_data)
            if response.status_code == 200:
                result = response.json()["response"]
                st.success(f"Predicted Category: {result['predicted_category']}")
                st.write(f"Confidence: {result['confidence']}")
                st.write("Class Probabilities:")
                st.json(result["class_probabilities"])
            else:
                st.error(f"API Error: {response.text}")
        except Exception as e:
            st.error(f"Connection error: {e}")
