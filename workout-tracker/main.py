import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://trackapi.nutritionix.com/v2/natural/exercise"

APPLICATION_ID = os.getenv("APPLICATION_ID")
API_KEY = os.getenv("API_KEY")
SHEETY_KEY = os.getenv("SHEETY_KEY")

print(APPLICATION_ID)
print(API_KEY)

today = datetime.now()

header = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

params = {
    "query": input("Enter the activity done for today: ")
}

res = requests.post(url = url, headers=header, json = params)
print(res.json())

metrics = res.json()
print(metrics['exercises'][0]['user_input'])

print(metrics['exercises'][0]['duration_min'])

print(metrics['exercises'][0]['nf_calories'])

#Now adding a row into sheety

sheety_url = "https://api.sheety.co/e243430d16f2cb6e37bea6b4edce7c78/workoutTracking/workouts"

header = {
    "Authorization": "Bearer mysecrettoken",
    "Content-Type": "application/json"
}

params = {
    "workout":  {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%X"),
        "exercise": metrics['exercises'][0]['user_input'],
        "duration": metrics['exercises'][0]['duration_min'],
        "calories": metrics['exercises'][0]['nf_calories']
    }
}

response = requests.post(url = sheety_url, headers=header, json = params )
print(response.text)