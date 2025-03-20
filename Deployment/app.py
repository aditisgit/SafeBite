import streamlit as st
from joblib import load
import numpy as np
import pandas as pd
import os

def find_file(filename, directory="."): 
    for root, _, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)

    return None  # File not found

# Function to safely load models
def safe_load(filename):
    file_path = find_file(filename)
    if file_path is None:
        raise FileNotFoundError(f"File '{filename}' not found in '{os.path.abspath('Models')}'.")
    return load(file_path)

# Load models safely
adulteration = safe_load("adulteration-prediction-model.joblib")
contamination = safe_load("contamination-prediction-model.joblib")
safety = safe_load("safety-classification-kmeans.joblib")

# Load encoders and scalers safely
contaminant_encoder = safe_load("contaminant_encoder.joblib")
foodgroup_encoder = safe_load("foodgroup_encoder.joblib")
result_scaler = safe_load("result_scaler.joblib")
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
    
    #selectbox lists
    countryNameList = ['HONG KONG SAR', 'Japan', 'China', 'Singapore', 'Thailand',
                        'India', 'Republic of Korea', 'Indonesia']
    
    foodGroupNameList = ['Legumes and pulses',
                        'Fish and other seafood (including amphibians, reptiles, snails and insects)',
                        'Vegetables and vegetable products (including fungi)',
                        'Starchy roots and tubers', 
                        'Milk and dairy products',
                        'Meat and meat products (including edible offal)',
                        'Fruit and fruit products', 
                        'Eggs and egg products']
    
    contaminantNameList = ['Ethyl carbamate', 'Other', 'Cesium 134', 'Cesium 137',
                            'Iodine 131', 'Cesium total', 'Dioxins (WHO TEFs)',
                            'Dioxin like PCBs (WHO TEFs)', 'Lead', 'Cadmium',
                            'Aflatoxin (total)', 'Aflatoxin G1', 'Aflatoxin G2', 'Tin',
                            'Aflatoxin B2', 'Copper', 'Mercury', 'Fumonisin B1', 'Patulin',
                            'Nitrite', 'Aflatoxin M1', 'Arsenic (total)', 'Aflatoxin B1',
                            'Arsenic (inorganic)', 'Deoxynivalenol',
                            '3-Chloro-1,2-propanediol', 'Ochratoxin A', 'Zearalenone',
                            'Hexachlorobenzene', 'Hexachlorocyclohexanes (HCH)',
                            'Fumonisin B2', 'Fumonisin B3', 'Pyrrolizidine alkaloids',
                            'Methyl mercury']
    
    #user inputs
    countryName = country_name = st.selectbox("Country Name", countryNameList, key = "c1")
    foodGroupName=st.selectbox("Food Group Name", foodGroupNameList, key = "c2")
    foodname= st.text_input("Food Name", key="c3")
    contaminantname= st.selectbox("Contaminant Name", contaminantNameList, key = "c4" )


    if st.button("Predict Contaminant Level", key="btn_c"):
        user_input = pd.DataFrame({
                'CountryName': countryName,
                'FoodGroupName': foodGroupName,
                'GEMSFoodName': foodname,
                'ContaminantName': contaminantname
        }, index = [0])
        
        preprocessed_input = contamination.named_steps['preprocessor'].transform(user_input)
        prediction_log = contamination.predict(user_input)
        prediction_original = np.expm1(prediction_log)[0]
        st.write(f"Contaminant Level: {prediction_original}")

# Safety Classification Tab
with tab3:
    st.header("Safety Classification")
    # Define dropdown options
    food_groups = [
        "Legumes and pulses",
        "Fish and other seafood (including amphibians, reptiles, snails and insects)",
        "Vegetables and vegetable products (including fungi)",
        "Starchy roots and tubers",
        "Milk and dairy products",
        "Meat and meat products (including edible offal)",
        "Fruit and fruit products",
        "Eggs and egg products"
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

    food_group_name = st.selectbox("Select Food Group", food_groups, key="s1")
    contaminant = st.selectbox("Select Contaminant", contaminants, key="s2")
    contaminant_quantity = st.number_input("Enter Quantity of Contaminant", key="s3")

    if st.button("Predict Safety", key="btn_s"):
        user_input = pd.DataFrame({
                        'FoodGroupEncoded': foodgroup_encoder.transform(food_group_name)[0],
                        'ContaminantEncoded': contaminant_encoder.transform(contaminant)[0],
                        'LogResultValue':result_scaler.transform(np.array([[contaminant_quantity]]))
        }, index = [0])
        safety_pred = safety.predict(user_input)
        st.write(f"Safety Prediction: {safety_pred}")
