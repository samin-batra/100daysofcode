import requests
from dotenv import load_dotenv
import os

KIWI_URL = "https://tequila-api.kiwi.com/v2"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.headers = {
            'apiKey': os.getenv('KIWI_API_KEY')
        }


    def search_flight(self, fly_from: str, date_from: str, date_to: str, return_date: str, return_future: str, max_price: int):
        params = {
            'fly_from': "DEL",
            'fly_to': fly_from,
            'date_from': date_from,
            'date_to': date_to,
            "price_to": 60000,
            "max_stopovers": 0,
            "curr": "INR",
            "return_from": return_date,
            "return_to": return_future

        }

        print(params)
        res = requests.get(url=f"{KIWI_URL}/search", headers=self.headers, params=params)
        data = []
        try:
            data = res.json()['data']
            return data
        except:
            return data


    def get_iata_codes(self, city_name: str):
        parameters = {
            "term": city_name
        }
        url = "https://tequila-api.kiwi.com"
        response = requests.get(f"{url}/locations/query", params=parameters, headers=self.headers)
        iata_data = response.json()
        loc_iata = {'iata': code['code'] for code in iata_data['locations'] if
                    code['name'].lower().strip() == city_name.lower().strip()}
        # data['iataCode'] = loc_iata['iata']
        # self.set_iata_code(data['iataCode'], data['id'])
        return loc_iata['iata']
