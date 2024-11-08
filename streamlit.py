import streamlit as st
import numpy as np
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
import joblib


# Define the function to run when the button is clicked
def calculate_price(zip_code, construction_year, number_rooms, living_area, kitchen_enc, primary_energy_consumption, double_glazing_enc, state_building_enc, type_house_enc):
    # Create a new XGBRegressor
    model = XGBRegressor()

    # load a saved XGBRegressor model
    model.load_model("./model/model_xgb.json")

    # load the saved scaler, to apply the same scaler
    scaler = joblib.load("./model/scaler.joblib")

    # create a new house and scale it
    new_house = np.array([zip_code, construction_year, number_rooms, living_area, kitchen_enc, primary_energy_consumption, double_glazing_enc, state_building_enc, type_house_enc]).reshape(1, -1)  #['Postal code', 'Construction year', 'Number of rooms', 'Living area','kitchen', 'Primary energy consumption', 'Double glazing','State_encoded', 'Type of property_house']
    new_data_scaled = scaler.transform(new_house)

    # predict the price of the new house
    predicted_price = model.predict(new_data_scaled)
    return predicted_price[0]

st.title('🧱House price prediction🧱')

st.info('This is an app to calculate the price of a house or apartment using a machine learning model')

st.write('You want to know the value of a house?')

type_house = st.selectbox("Is it a house or an apartement?", ('House', 'Apartment'), index=None, placeholder="Select house or apartment")
if type_house == 'House':
    type_house_enc = 1
else:
    type_house_enc = 0
try:
    zip_code = int(st.text_input("What is the zip code?", value=0))
except ValueError as ve:
    st.error(f"Please enter a valid numeric value")
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
    try:
        price = calculate_price(zip_code, construction_year, number_rooms, living_area, kitchen_enc, primary_energy_consumption, double_glazing_enc, state_building_enc, type_house_enc)
        if type_house_enc == 1:
            st.info("House with the parameters:")
            st.write("Type: house")
        else:
            st.info("Apartment with the parameters:")
            st.write("Type: apartment")
        st.write("Zip code: ", zip_code)
        st.write("construction year: ", construction_year)
        st.write("Number of rooms: ", number_rooms)
        st.write("living_area: ", living_area, " m²")
        if kitchen_enc == 1:
            st.write("Kitchen: equipped")
        else:
            st.write("Kitchen: not equipped")
        st.write("primary energy consumption : ", primary_energy_consumption, " kWh/m²")
        if double_glazing_enc == 1:
            st.write("Double glazing: present")
        else:
            st.write("Double glazing: not present")
        st.write("State of the building: ", state_building)
        
        st.info("Your predicted price: €", round(price))
    except ValueError as ve:
        st.error(f"Please enter valid values")     

    
