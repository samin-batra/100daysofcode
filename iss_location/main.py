import math
import time
import smtplib

import requests
from datetime import datetime

MY_LAT = 28.6139
MY_LONG = 77.2090
MY_EMAIL = "doejohnny160@gmail.com"
MY_PASSWORD = "Hello@123"


def check_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", parameters)
    response.raise_for_status()
    result = response.json()
    print(response.json())
    sunrise = result['results']['sunrise']
    sunset = result['results']['sunset']
    sunrise_hour = int(sunrise.split('T')[1].split(':')[0])
    sunset_hour = int(sunset.split('T')[1].split(':')[0])
    my_time = datetime.now()
    my_hour = my_time.hour
    if sunset_hour < my_hour < sunrise_hour:
        return True


def check_iss_passing():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    curr_pos = response.json()
    lng = float(curr_pos['iss_position']['longitude'])
    lat = float(curr_pos['iss_position']['latitude'])
    if math.fabs(lng - MY_LONG) < 5 and math.fabs(lat - MY_LAT) < 5:
        return True


def send_mail():
    connect = smtplib.SMTP(host='smtp.gmail.com')
    connect.starttls()
    connect.login(user=MY_EMAIL, password=MY_PASSWORD)
    connect.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                     msg="Subject: ISS Passing! \n\n Look up! The ISS is passing over your place right now!")


while True:
    if check_night():
        if check_iss_passing():
            send_mail()
    time.sleep(60)
