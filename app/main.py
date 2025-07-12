
import streamlit as st 
import requests


st.set_page_config(page_title="vehicle insurance prediction", page_icon="🚗")

st.title("🚗 Vehicle Insurance Prediction")
st.markdown("Enter your details below:")

APP_URL = "http://localhost:8000/predict"

gender = st.selectbox("Select your gender",options=["Male","Female"])
age = st.number_input("Age", min_value=1, max_value=119, value=30)
driving_license = st.selectbox("Do you have driving license",options=[0,1])
region_code = st.number_input("Region Code",min_value=0, step=1, format="%d")
previously_insured = st.selectbox("Do you insured previously",options=[0,1])
vehicle_demage = st.selectbox("Are your vehicke demage",options=["Yes","No"])
annual_premium = st.number_input("Annual_Premium")
Vehicle_Age_lt_1_Year = st.selectbox("Is your Vehicle age less than 1 year or not", options=[0,1])
Vehicle_Age_gt_1_Year = st.selectbox("Is your Vehicle age greater than 1 year or not", options=[0,1])


if st.button("Get Your Prediction !!"):
    input_data = {
    'gender': gender,
    'age': age,
    'driving_license': driving_license,
    'region_code': region_code,
    'previously_insured': previously_insured,
    'vehicle_damage': vehicle_demage,
    'annual_premium': annual_premium,
    'Vehicle_Age_lt_1_Year': Vehicle_Age_lt_1_Year,
    'Vehicle_Age_gt_1_Year': Vehicle_Age_gt_1_Year
    }
    
    try:
        response = requests.post(APP_URL, json=input_data)
        result = response.json()
        if response.status_code == 200 and "response" in result:
            prediction = result["response"]
            st.success(f"Do you get a vehicle insurance? : {'✅ Yes' if prediction['predicted_class'] == 1 else '❌ No'}")
            st.write("🔍 Confidence:", prediction["confidence"])
            st.write("📊 Class Probabilities:")
            st.json(prediction["class_probabilities"])
        else:
            st.error(f"API Error: {response.status_code}")
            st.write(result)
    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")

