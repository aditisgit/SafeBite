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

# Create tabs
tab1, tab2, tab3 = st.tabs(["Adulteration Prediction", "Contaminant Level Prediction", "Safety Classification"])

# Adulteration Prediction Tab
with tab1:
    st.header("Adulteration Prediction")
    feature1 = st.number_input("Enter feature 1", key="a1")
    feature2 = st.number_input("Enter feature 2", key="a2")
    feature3 = st.number_input("Enter feature 3", key="a3")
    feature4 = st.number_input("Enter feature 4", key="a4")

    if st.button("Predict Adulteration", key="btn_a"):
        user_input = np.array([[feature1, feature2, feature3, feature4]])
        adulteration_pred = adulteration.predict(user_input)
        st.write(f"Adulteration Prediction: {adulteration_pred}")

# Contaminant Level Prediction Tab
with tab2:
    st.header("Contaminant Level Prediction")
    feature1 = st.number_input("Enter feature 1", key="c1")
    feature2 = st.number_input("Enter feature 2", key="c2")
    feature3 = st.number_input("Enter feature 3", key="c3")
    feature4 = st.number_input("Enter feature 4", key="c4")

    if st.button("Predict Contaminant Level", key="btn_c"):
        user_input = np.array([[feature1, feature2, feature3, feature4]])
        contaminant_pred = contamination.predict(user_input)
        st.write(f"Contaminant Level: {contaminant_pred}")

# Safety Classification Tab
with tab3:
    st.header("Safety Classification")
    feature1 = st.number_input("Enter feature 1", key="s1")
    feature2 = st.number_input("Enter feature 2", key="s2")
    feature3 = st.number_input("Enter feature 3", key="s3")
    feature4 = st.number_input("Enter feature 4", key="s4")

    if st.button("Predict Safety", key="btn_s"):
        user_input = np.array([[feature1, feature2, feature3, feature4]])
        safety_pred = safety.predict(user_input)
        st.write(f"Safety Classification: {'Safe' if safety_pred == 1 else 'Unsafe'}")
