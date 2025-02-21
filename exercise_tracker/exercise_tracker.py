import requests
import os
from dotenv import find_dotenv, load_dotenv
from datetime import datetime as dt

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
GENDER = "male"
WEIGHT = 75
HEIGHT = 170
AGE = 26
DATE = dt.now().strftime("%d/%m/%Y")
TIME = dt.now().strftime("%X")
AUTH_USER = os.environ.get("AUTH_USER")
AUTH_PASS = os.environ.get("AUTH_PASS")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_input = input("Which exercise did you do? ")

sheety_endpoint = "https://api.sheety.co/35778f292b39d6101405b09da25998f7/workoutTracking/workouts"

HEADERS = {
    "x-app-id" : APP_ID,
    "x-app-key" : APP_KEY,
}

nutritionix_params = {
    "query" : exercise_input,
    "gender" : GENDER,
    "weight_kg" : WEIGHT,
    "height_cm" : HEIGHT,
    "age" : AGE,
}

nut_response = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers=HEADERS)
nut_response.raise_for_status()
nut = nut_response.json()["exercises"][0]

sheety_params = {
    "workout" : {
        "date" : DATE,
        "time" : TIME,
        "exercise" : nut["name"].title(),
        "duration" : nut["duration_min"],
        "calories" : nut["nf_calories"],
    }
}

sheety_response = requests.post(url=sheety_endpoint, json=sheety_params, auth=(AUTH_USER, AUTH_PASS))
sheety_response.raise_for_status()

