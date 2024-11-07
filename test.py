import requests

url = "http://127.0.0.1:8000/predict"
data = {
    "postal_code": 1000,
    "construction_year": 2000,
    "number_of_rooms": 3,
    "living_area": 120.5,
    "kitchen": 1.0,
    "primary_energy_consumption": 80.0,
    "double_glazing": 1,
    "state_encoded": 2,
    "type_of_property_house": 1
}

response = requests.post(url, json=data)
print(response.json())