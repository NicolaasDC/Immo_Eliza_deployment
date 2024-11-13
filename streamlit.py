import streamlit as st
import numpy as np
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
import joblib
import requests


st.title('🧱House price prediction🧱')

st.info('This is an app to calculate the price of a house or apartment in Belgium using a machine learning model')

st.write('You want to know the value of a house?')

type_house = st.selectbox("Is it a house or an apartement?", ('House', 'Apartment'), index=None, placeholder="Select house or apartment")
if type_house == 'House':
    type_house_enc = 1
else:
    type_house_enc = 0
try:
    zip_code = int(st.text_input("What is the zip code?", value=0))
    if not (1000 <= zip_code <= 9992):
        st.error("Please enter a numeric value between 1000 and 9992")
except ValueError as ve:
    st.error(f"Please enter a valid numeric value between 1000 and 9992")
try:
    construction_year = int(st.text_input("What is the construction year?", value=0))
except ValueError as ve:
    st.error(f"Please enter a valid numeric value")
try:
    number_rooms = int(st.text_input("What is the number of rooms?", value=0))
except ValueError as ve:
    st.error(f"Please enter a valid numeric value{ve}")
try:
    living_area = float(st.text_input("What is the living area? (m²)", value=0))
except ValueError as ve:
    st.error(f"Please enter a valid numeric value: {ve}")
    
kitchen = st.selectbox("Is a kitchen equipped?", ("Yes", "No"), index=None,
    placeholder="Select kitchen")
if kitchen ==  'Yes':
    kitchen_enc = 1
else:
    kitchen_enc = 0
try:
    primary_energy_consumption = float(st.text_input("What is the primary energy consumption? (kWh/m²)", value=0))
except ValueError as ve:
    st.error(f"Please enter a valid numeric value")
    
double_glazing = st.selectbox("Does the house have double glazing?",('Yes', 'No'), index=None, placeholder="Select double glazing")
if double_glazing ==  'Yes':
    double_glazing_enc = 1
else:
    double_glazing_enc = 0

state_building = st.selectbox("What is the state of the building?", ('To restore', 'To renovate', 'To be done up', 'Good', 'Just renovated', 'As new'), index=None, placeholder="Select state of the building")
state_encoded = {'To restore': 0, 'To renovate': 1, 'To be done up': 2, 'Good': 3, 'Just renovated': 4, 'As new': 5}

state_building_enc = state_encoded.get(state_building, 0)
    
# Place the button in the Streamlit app
if st.button("Click to calculate price"):
# Call the function when the button is clicked
    if zip_code == 0 or construction_year == 0 or number_rooms == 0 or living_area == 0 or primary_energy_consumption == 0:
        st.error("Please fill in all required fields (numeric fields must be non-zero).")
    else:
        try:
            url = "https://immo-eliza-deployment-2ak3.onrender.com/predict"
            data = {
                "postal_code": zip_code,
                "construction_year": construction_year,
                "number_of_rooms": number_rooms,
                "living_area": living_area,
                "kitchen": kitchen_enc,
                "primary_energy_consumption": primary_energy_consumption,
                "double_glazing": double_glazing_enc,
                "state_encoded": state_building_enc,
                "type_of_property_house": type_house_enc
            }

            response = requests.post(url, json=data)
            if response.status_code != 200:
                st.error("API request failed. Status code: " + str(response.status_code))
            else:
                price = response.json().get('prediction', 'Prediction not available')
            
            if type_house_enc == 1:
                st.info("House with the parameters:")
                st.write("Type: house")
            else:
                st.info("Apartment with the parameters:")
                st.write("Type: apartment")
            st.write(f"Zip code: {zip_code}")
            st.write(f"construction year: {construction_year}")
            st.write(f"Number of rooms: {number_rooms}")
            st.write(f"living area: {living_area} m²")
            if kitchen_enc == 1:
                st.write("Kitchen: equipped")
            else:
                st.write("Kitchen: not equipped")
            st.write(f"primary energy consumption: {primary_energy_consumption} kWh/m²")
            if double_glazing_enc == 1:
                st.write("Double glazing: present")
            else:
                st.write("Double glazing: not present")
            st.write(f"State of the building: {state_building}")
            
            st.info(f"Your predicted price: € {price}")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    
