import streamlit as st

st.title('🤖House price prediction🤖')

st.info('This is a machine learning app')

st.write('You want to know the value of a house')
zip_code = st.text_input("What is the zip code?")
