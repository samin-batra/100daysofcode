from datetime import datetime


class FlightData:
    # This class is responsible for structuring the flight data.

    def __init__(self):
        self.flight_info = {
            "departure_city": "",
            "arrival_city": "",
            "departure_airport": "",
            "arrival_airport": "",
            "departure_date": "",
            "return_date": "",
            "price": 0
        }

    def set_flight_info(self, data):
        self.flight_info["departure_city"] = data['cityFrom']
        self.flight_info["arrival_city"] = data['cityTo']
        self.flight_info["departure_airport"] = data['flyFrom']
        self.flight_info["arrival_airport"] = data['flyTo']
        dep_date = datetime.strptime(data['route'][0]['local_departure'], "%Y-%m-%dT%H:%M:%S.%fZ")
        ret_date = datetime.strptime(data['route'][1]['local_arrival'], "%Y-%m-%dT%H:%M:%S.%fZ")
        self.flight_info["departure_date"] = dep_date.strftime("%Y-%m-%d")
        self.flight_info["return_date"] = ret_date.strftime("%Y-%m-%d")
        self.flight_info["price"] = data['price']
        print(self.flight_info)
