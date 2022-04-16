import requests
import os
from twilio.rest import Client

API_KEY = os.environ.get('API_KEY')

params = {
    "lat":10.850516,
    "lon":76.271080,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

url = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = os.environ.get('SID_TWILIO')
auth_token = os.environ.get('AUTH_TOKEN_TWILIO')

res = requests.get(url,params)
res.raise_for_status()
print(res.status_code)
weather_data = res.json()
# print(weather_data)
hourly_next_12 = weather_data['hourly'][0:12]
print(hourly_next_12)
will_rain = False
# rain = [True for h in hourly_next_12 if h['weather']
for h in hourly_next_12:
    for w in h['weather']:
        if w['id']<600:
            will_rain = True
            print("Bring an umberella!")


if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Do make sure to carry an umberella!",
        from_='+12058517950',
        to='+919810116672'
    )
    print(message.sid)
