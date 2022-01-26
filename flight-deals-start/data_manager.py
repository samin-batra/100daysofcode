import requests
import os
from dotenv import load_dotenv
import pandas as pd


PRICES_URL_GET = "https://api.sheety.co/e243430d16f2cb6e37bea6b4edce7c78/flightDealFinder/prices"
KIWI_URL = "https://tequila-api.kiwi.com"
PRICES_URL_PUT = "https://api.sheety.co/e243430d16f2cb6e37bea6b4edce7c78/flightDealFinder/prices/"


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        load_dotenv()
        self.header = {
            'Authorization': f"Bearer {os.getenv('SHEETY_API_TOKEN')}"
        }


        # response = requests.get(PRICES_URL_GET, headers=self.header)

        # print(response.text)
        # self.sheet_data = response.json()['prices']
        loc_data = pd.read_csv("flights.csv")
        print(loc_data)
        self.sheet_data = loc_data.to_dict(orient="records")

    def write_data(self):
        sheet_df = pd.DataFrame(self.sheet_data)
        sheet_df.to_csv("flights.csv", index = False)

    def set_iata_code(self, iata_code: str, id: str):
        data = {
            'price': {
                'iataCode': iata_code
            }
        }
        res = requests.put(f"{PRICES_URL_PUT}/{id}", headers=self.header, json=data)
        # print(res.text)
