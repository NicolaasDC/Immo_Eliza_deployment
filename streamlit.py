import streamlit as st

def calculate_price(zip_code, construction_year, number_rooms, living_area, kitchen_enc, primary_energy_consumption, double_glazing_enc, state_building_enc, type_house_enc)

st.title('🧱House price prediction🧱')

st.info('This is app to calculate the price of a house using a machine learning model')

st.write('You want to know the value of a house?')
zip_code = st.text_input("What is the zip code?")

construction_year = st.text_input("What is the construction year?")

number_rooms = st.text_input("What is the number of rooms?")

living_area = st.text_input("What is the living area? (m²)")

kitchen = st.selectbox("Is a kitchen equipped?", ("Yes", "No"), index=None,
    placeholder="Select kitchen")
if kitchen ==  'Yes':
    kitchen_enc = 1
if kitchen ==  'No':
    kitchen_enc = 0

primary_energy_consumption = st.text_input("What is the primary energy consumption? (kWh/m²)")

double_glazing = st.selectbox("Does the house have double glazing?",('Yes', 'No'), index=None, placeholder="Select double glazing")
if double_glazing ==  'Yes':
    double_glazing_enc = 1
if double_glazing ==  'No':
    double_glazing_enc = 0

state_building = st.selectbox("What is the state of the building?", ('To restore', 'To renovate', 'To be done up', 'Good', 'Just renovated', 'As new'), index=None, placeholder="Select state of the building")
state_encoded = {'To restore': 0, 'To renovate': 1, 'To be done up': 2, 'Good': 3, 'Just renovated': 4, 'As new': 5}
state_building_enc = state_encoded[state_building]


type_house = st.selectbox("Is it a house or an apartement?", ['House', 'Apartment'], index=None, placeholder="Select house or apartment")
if type_house == 'House':
    type_house_enc = 1
if type_house == 'Apartment':
    type_house_enc = 0