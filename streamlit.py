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

st.info('This is an app to calculate the price of a house using a machine learning model')

st.write('You want to know the value of a house?')
try:
    zip_code = int(st.text_input("What is the zip code?", value=0))

    construction_year = int(st.text_input("What is the construction year?", value=0))

    number_rooms = int(st.text_input("What is the number of rooms?", value=0))

    living_area = float(st.text_input("What is the living area? (m²)", value=0))

    kitchen = st.selectbox("Is a kitchen equipped?", ("Yes", "No"), index=None,
        placeholder="Select kitchen")
    if kitchen ==  'Yes':
        kitchen_enc = 1
    else:
        kitchen_enc = 0

    primary_energy_consumption = float(st.text_input("What is the primary energy consumption? (kWh/m²)", value=0))

    double_glazing = st.selectbox("Does the house have double glazing?",('Yes', 'No'), index=None, placeholder="Select double glazing")
    if double_glazing ==  'Yes':
        double_glazing_enc = 1
    else:
        double_glazing_enc = 0

    state_building = st.selectbox("What is the state of the building?", ('To restore', 'To renovate', 'To be done up', 'Good', 'Just renovated', 'As new'), index=None, placeholder="Select state of the building")
    state_encoded = {'To restore': 0, 'To renovate': 1, 'To be done up': 2, 'Good': 3, 'Just renovated': 4, 'As new': 5}

    state_building_enc = state_encoded[state_building]


    type_house = st.selectbox("Is it a house or an apartement?", ('House', 'Apartment'), index=None, placeholder="Select house or apartment")
    if type_house == 'House':
        type_house_enc = 1
    else:
        type_house_enc = 0
    
        # Place the button in the Streamlit app
    if st.button("Click to calculate price"):
        # Call the function when the button is clicked
        price = calculate_price(zip_code, construction_year, number_rooms, living_area, kitchen_enc, primary_energy_consumption, double_glazing_enc, state_building_enc, type_house_enc)   
        st.write("Your predicted price: €", round(price, 2))
        
except ValueError as ve:
    st.error(f"Please enter valid numeric values for all inputs: {ve}")
    
