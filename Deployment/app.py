import streamlit as st
from joblib import load
import numpy as np
import pandas as pd
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
    feature1 = st.text_input("Enter feature 1", key="a1")
    feature2 = st.text_input("Enter feature 2", key="a2")
    feature3 = st.number_input("Enter feature 3", key="a3")
    feature4 = st.number_input("Enter feature 4", key="a4")

    if st.button("Predict Adulteration", key="btn_a"):
        user_input = np.array([[feature1, feature2, feature3, feature4]])
        adulteration_pred = adulteration.predict(user_input)
        st.write(f"Adulteration Prediction: {adulteration_pred}")

# Contaminant Level Prediction Tab
with tab2:
    st.header("Contaminant Level Prediction")
    countryName = country_name = st.selectbox("Country Name", 
                                              ['HONG KONG SAR', 'Japan', 'China', 'Singapore', 'Thailand',
                                                'India', 'Republic of Korea', 'Indonesia'])
    
    foodGroupName=st.selectbox("Food Group Name",
                               ['Legumes and pulses',
                                'Fish and other seafood (including amphibians, reptiles, snails and insects)',
                                'Vegetables and vegetable products (including fungi)',
                                'Starchy roots and tubers', 
                                'Milk and dairy products',
                                'Meat and meat products (including edible offal)',
                                'Fruit and fruit products', 
                                'Eggs and egg products'])
    
    foodname= st.text_input("Food Name", key="c3")
    
    contaminantname= st.selectbox("Contaminant Name", 
                                  ['Ethyl carbamate', 'Other', 'Cesium 134', 'Cesium 137',
                                    'Iodine 131', 'Cesium total', 'Dioxins (WHO TEFs)',
                                    'Dioxin like PCBs (WHO TEFs)', 'Lead', 'Cadmium',
                                    'Aflatoxin (total)', 'Aflatoxin G1', 'Aflatoxin G2', 'Tin',
                                    'Aflatoxin B2', 'Copper', 'Mercury', 'Fumonisin B1', 'Patulin',
                                    'Nitrite', 'Aflatoxin M1', 'Arsenic (total)', 'Aflatoxin B1',
                                    'Arsenic (inorganic)', 'Deoxynivalenol',
                                    '3-Chloro-1,2-propanediol', 'Ochratoxin A', 'Zearalenone',
                                    'Hexachlorobenzene', 'Hexachlorocyclohexanes (HCH)',
                                    'Fumonisin B2', 'Fumonisin B3', 'Pyrrolizidine alkaloids',
                                    'Methyl mercury'])


    if st.button("Predict Contaminant Level", key="btn_c"):
        user_input = pd.DataFrame({
                'CountryName': countryName,
                'FoodGroupName': foodGroupName,
                'GEMSFoodName': foodname,
                'ContaminantName': contaminantname
        })
        
        prediction_log = contamination.predict(user_input)
        prediction_original = np.expm1(prediction_log)[0]
        st.write(f"Contaminant Level: {prediction_original}")

# Safety Classification Tab
# Load saved KMeans model
safety_model_path = find_file("safety-classification-kmeans.joblib")
safety = load(safety_model_path) if safety_model_path else None

# Load saved LabelEncoders
foodgroup_encoder_path = find_file("foodgroup_encoder.joblib")
label_encoders = load(foodgroup_encoder_path) if foodgroup_encoder_path else None

contaminant_encoder_path = find_file("contaminant_encoder.joblib")
label_encoders = load(contaminant_encoder_path) if contaminant_encoder_path else None

# Load saved StandardScaler
scaler_path = find_file("result_scaler.joblib")
scaler = load(scaler_path) if scaler_path else None


# Define dropdown options
food_groups = [
    "Legumes and pulses", "Fish and other seafood (including amphibians, reptiles, snails and insects)",
    "Vegetables and vegetable products (including fungi)", "Starchy roots and tubers",
    "Milk and dairy products", "Meat and meat products (including edible offal)",
    "Fruit and fruit products", "Eggs and egg products"
]

contaminants = [
    "Ethyl carbamate", "Other", "Cesium 134", "Cesium 137", "Iodine 131",
    "Cesium total", "Dioxins (WHO TEFs)", "Dioxin like PCBs (WHO TEFs)", "Lead",
    "Cadmium", "Aflatoxin (total)", "Aflatoxin G1", "Aflatoxin G2", "Tin",
    "Aflatoxin B2", "Copper", "Mercury", "Fumonisin B1", "Patulin", "Nitrite",
    "Aflatoxin M1", "Arsenic (total)", "Aflatoxin B1", "Arsenic (inorganic)",
    "Deoxynivalenol", "3-Chloro-1,2-propanediol", "Ochratoxin A", "Zearalenone",
    "Hexachlorobenzene", "Hexachlorocyclohexanes (HCH)", "Fumonisin B2",
    "Fumonisin B3", "Pyrrolizidine alkaloids", "Methyl mercury"
]

with tab3:
    st.header("Safety Classification")

    # User Inputs
    food_group_name = st.selectbox("Select Food Group", food_groups, key="s1")
    contaminant = st.selectbox("Select Contaminant", contaminants, key="s2")
    contaminant_quantity = st.number_input("Enter Quantity of Contaminant", key="s3")

    if st.button("Predict Safety", key="btn_s"):
        if safety and label_encoders and scaler:
            # Encode categorical features using saved LabelEncoders
            if food_group_name in label_encoders["food_group"].classes_:
                food_group_encoded = label_encoders["food_group"].transform([food_group_name])[0]
            else:
                food_group_encoded = -1  # Handle unseen categories

            if contaminant in label_encoders["contaminant"].classes_:
                contaminant_encoded = label_encoders["contaminant"].transform([contaminant])[0]
            else:
                contaminant_encoded = -1  # Handle unseen categories

            # Prepare input for prediction
            user_input = np.array([[food_group_encoded, contaminant_encoded, contaminant_quantity]])

            # Scale the numerical feature (contaminant quantity)
            user_input[:, 2:] = scaler.transform(user_input[:, 2:])

            # Make prediction
            safety_pred = safety.predict(user_input)

            # Display result
            st.write(f"Safety Prediction: {safety_pred}")
        else:
            st.error("Safety classification model, label encoders, or scaler not found.")
