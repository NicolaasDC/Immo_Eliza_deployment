import pandas as pd
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from xgboost import XGBRegressor
from sklearn.preprocessing import StandardScaler
import joblib


# Create the app

app = FastAPI()

# Create a new XGBRegressor
model = XGBRegressor()

# Load trained Pipeline
model.load_model("./model/model_xgb.json")


# Load the saved scaler
scaler = joblib.load("./model/scaler.joblib")

# Define a request body model
class HouseData(BaseModel):
    postal_code: int
    construction_year: int
    number_of_rooms: int
    living_area: float
    kitchen: float
    primary_energy_consumption: float
    double_glazing: int
    state_encoded: int
    type_of_property_house: int

@app.get("/")
async def root():
    return {"Server": "Alive"}

# Define predict function
@app.post('/predict')
def predict(data: HouseData):
    # Create a new house and scale it
    new_house = np.array([[
        data.postal_code,
        data.construction_year,
        data.number_of_rooms,
        data.living_area,
        data.kitchen,
        data.primary_energy_consumption,
        data.double_glazing,
        data.state_encoded,
        data.type_of_property_house
    ]])
    
    # Scale the new data
    new_data_scaled = scaler.transform(new_house)

    # Predict the price
    predicted_price = model.predict(new_data_scaled)

    return {'prediction': round(float(predicted_price[0]),0)}

# Run the app
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)