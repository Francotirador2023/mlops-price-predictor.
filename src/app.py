import streamlit as st
import requests
import json

st.set_page_config(page_title="House Price Predictor", page_icon="🏠")

st.title("🏠 California House Price Predictor")
st.markdown("Enter the housing details below to get an estimated price.")

# Sidebar for inputs
st.sidebar.header("Input Features")

med_inc = st.sidebar.slider("Median Income (in 10k)", 0.5, 15.0, 3.0)
house_age = st.sidebar.slider("House Age", 1, 52, 20)
ave_rooms = st.sidebar.slider("Average Rooms", 1.0, 10.0, 5.0)
ave_bedrms = st.sidebar.slider("Average Bedrooms", 0.5, 5.0, 1.0)
population = st.sidebar.slider("Population", 100, 5000, 1000)
ave_occup = st.sidebar.slider("Average Occupancy", 1.0, 10.0, 3.0)
latitude = st.sidebar.number_input("Latitude", 32.0, 42.0, 34.0)
longitude = st.sidebar.number_input("Longitude", -124.0, -114.0, -118.0)

features = {
    "MedInc": med_inc,
    "HouseAge": house_age,
    "AveRooms": ave_rooms,
    "AveBedrms": ave_bedrms,
    "Population": population,
    "AveOccup": ave_occup,
    "Latitude": latitude,
    "Longitude": longitude
}

if st.button("Predict Price", type="primary"):
    API_URL = "http://127.0.0.1:8000/predict"
    
    try:
        response = requests.post(API_URL, json=features)
        if response.status_code == 200:
            result = response.json()
            price_usd = result["predicted_price_usd"]
            st.success(f"Estimated Price: ${price_usd:,.2f}")
            st.balloons()
            
            # Additional details
            st.json(result)
        else:
            st.error(f"Error: {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to API. Is it running?")
