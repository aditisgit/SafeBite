import streamlit as st
from joblib import load
import numpy as np
import os

def find_file(filename, directory="."):
    for root, _, files in os.walk(directory):
        if filename in files:
            return fr"{os.path.join(root, filename)}"  # Return raw string format

    return None  # File not found

# Load saved models
adulteration = load("" if find_file("adulteration-prediction-model.joblib") is None else find_file("adulteration-prediction-model.joblib"))
contamination = load("" if find_file("contamination-prediction-model.joblib") is None else find_file("contamination-prediction-model.joblib"))
safety = load("" if find_file("safety-classification-kmeans.joblib") is None else find_file("safety-classification-kmeans.joblib"))

# Streamlit UI
st.title("Food Adulteration & Contamination Detection")

# User inputs
feature1 = st.number_input("Enter feature 1")
feature2 = st.number_input("Enter feature 2")
feature3 = st.number_input("Enter feature 3")
feature4 = st.number_input("Enter feature 4")

if st.button("Predict"):
    user_input = np.array([[feature1, feature2, feature3, feature4]])

    # Predictions from models
    adulteration_pred = adulteration.predict(user_input)
    contaminant_pred = contamination.predict(user_input)
    safety_pred = safety.predict(user_input)

    st.write(f"Adulteration Prediction: {adulteration_pred}")
    st.write(f"Contaminant Level: {contaminant_pred}")
    st.write(f"Safety Classification: {'Safe' if safety_pred == 1 else 'Unsafe'}")
