# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from datetime import datetime
from datetime import timedelta
from notification_manager import NotificationManager

data = DataManager()
flights = FlightSearch()
print(data.sheet_data)

for row in data.sheet_data:
    if row['IATA Code'] != row['IATA Code']:
        print(row['City'])
        iata_code = flights.get_iata_codes(row['City'])
        print(iata_code)
        row['IATA Code'] = iata_code

data.write_data()

curr_date = datetime.now()
future_date: datetime
return_date: datetime
return_future_date: datetime

future_date = curr_date + timedelta(days=180)
return_date = curr_date + timedelta(days=10)
return_future_date = return_date + timedelta(days=180)

for row in data.sheet_data:
    if row['IATA Code'] != None:
        returned_data = flights.search_flight(row['IATA Code'], curr_date.strftime("%d/%m/%Y"),
                                              future_date.strftime("%d/%m/%Y"), return_date.strftime("%d/%m/%Y"),
                                              return_future_date.strftime("%d/%m/%Y"), int(row['Lowest Price']))
        # print(type(returned_data))
        if len(returned_data) != 0:
            # print(returned_data)
            flight_data = FlightData()
            flight_data.set_flight_info(returned_data[0])
            notification = NotificationManager()
            notification.send_message(flight_data.flight_info)
