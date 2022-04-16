from dotenv import load_dotenv
import os
from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        load_dotenv()
        self.TWILIO_ACT_ID = os.getenv("TWILIO_ACT_ID")
        self.TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")


    def send_message(self, flight_data):
        client = Client(self.TWILIO_ACT_ID, self.TWILIO_AUTH_TOKEN)
        message = f"Low price alert! Fly from {flight_data['departure_city']}-{flight_data['departure_airport']} to {flight_data['arrival_city']}-{flight_data['arrival_airport']} at INR{flight_data['price']} departure on {flight_data['departure_date']} and return on {flight_data['return_date']}"
        message = client.messages.create(
            body = message,
            from_ ='+12058517950',
            to='+919810116672'
        )

        print(message.sid)
