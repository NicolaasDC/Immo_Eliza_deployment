import streamlit as st

st.title('🧱House price prediction🧱')

st.info('This is a machine learning app')

st.write('You want to know the value of a house?')
zip_code = st.text_input("What is the zip code?")

construction_year = st.text_input("What is the construction year?")

number_rooms = st.text_input("What is the number of rooms?")

living_area = st.text_input("What is the living area?")

kitchen = st.text_input("Is a kitchen equipped?")

primary_energy_consumption = st.text_input("What is the primary energy consumption?")

double_glazing = st.text_input("Does the house have double glazing?")

state_building = st.text_input("What is the state of the building?")

type_house = st.text_input("Is it a house or an apartement?")
