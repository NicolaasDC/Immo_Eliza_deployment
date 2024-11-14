# Immo_Eliza_deployment


# Description

The real estate company Immo Eliza asked you to create a machine learning model to predict prices of real estate properties in Belgium. 
This document describes the final stage of the project: model deployment.

This project follows previous stages in the immo-eliza-scraping (https://github.com/NicolaasDC/immo-eliza-scraping), 
immo-eliza-data-analysis project (https://github.com/VB1395/immoeliza_data_analysis) and 
immo_eliza_ML (https://github.com/NicolaasDC/Immo_Eliza_ML) repositories.


# Objectives
```
- Deploy a machine learning model via an API endpoint.
- Host the API on Render. 
- Build a simple web application using Streamlit.
```
# Repo structure
```
.
├── .gitignore
├── model/
│   ├── model_xgb.json
│   └── scaler.joblib
├── Dockerfile
├── main.py
├── streamlit.py
├── requirements.txt
└── README.md
```

# Usage

The Streamlit page is hosted here: https://immoelizadeployment.streamlit.app/.

The streamlit.py file creates the front-end app interface on Streamlit. 
The app accepts input for all features, then sends a request to the API's /predict endpoint to calculate the predicted price.
Once the button is clicked, the API responds with the predicted price, and a summary of the house and price is displayed.

The API is defined in main.py and hosted on Render using a Dockerfile. 
The link to the API is: https://immo-eliza-deployment-2ak3.onrender.com

# Timeline

This project took four days to complete, which included studying the subject matter.

# Addition info

This project was done as part of the AI Bootcamp at BeCode.org.

