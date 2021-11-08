import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 175
AGE = 17

APP_ID = "5180984f"
API_KEY = "f86a15c219299f407fceaf15a97a2871"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()


now = datetime.today().strftime('%m/%d/%Y')
current_hour = datetime.now().hour
current_minute = datetime.now().minute
current_time = f"{current_hour}:{current_minute}"

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("workout-tracker-331503-92fddb8799cd.json", scope)

client = gspread.authorize(creds)
sheet = client.open("MyWorkouts").sheet1
row = sheet.row_values(2)
insertRow = [now, current_time, result["exercises"][0]['name'], result["exercises"][0]['duration_min'], result["exercises"][0]['nf_calories']]

sheet.insert_row(insertRow, 2)

