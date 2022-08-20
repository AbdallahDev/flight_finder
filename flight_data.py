import datetime
from datetime import timedelta
import os

import requests

# from data_manager import DataManager

# /locations/query
ENDPOINT = os.environ['ENDPOINT_TEQUILA']
SEARCH_API = 'v2/search'
LOCATION_API = 'locations/query'
API_KEY = os.environ['APIKEY_TEQUILA']
HEADERS = {"accept": "application/json", "apikey": API_KEY}
LOCALE = 'en-US'
LOCATION_TYPES = 'city'
LIMIT = 1
LOCATION_API_PARAMS = {
    'locale': LOCALE,
    'location_types': LOCATION_TYPES,
    'limit': LIMIT,
}
GOOD_DEALS = []


class FlightData:
    def __init__(self, row_data: dict):
        self.row_data = row_data

    def city_code(self) -> str:
        LOCATION_API_PARAMS.update({'term': self.row_data['city']})
        req = requests.get(url=ENDPOINT + LOCATION_API,
                           headers=HEADERS, params=LOCATION_API_PARAMS)
        req.raise_for_status()
        data = req.json()
        code = data['locations'][0]['code']

        return code

    def lowest_price(self):
        date_from = datetime.date.today() + datetime.timedelta(days=1)
        date_to = date_from + datetime.timedelta(days=16)
        return_from = date_to + datetime.timedelta(days=16)
        return_to = return_from + datetime.timedelta(days=16)
        params = {'fly_from': 'AMM', 'fly_to': self.row_data['iataCode'],
                  'date_from': date_from, 'date_to': date_to,
                  'return_from': return_from,
                  'return_to': return_to,
                  'flight_type': 'round',
                  'one_for_city': 1,
                  'vehicle_type': 'aircraft',
                  'curr': 'JOD',
                  'adults': 1,
                  }
        req = requests.get(
            url=ENDPOINT + SEARCH_API,
            params=params,
            headers=HEADERS
        )
        req.raise_for_status()
        data = req.json()
        flight = {}
        try:
            flight = data['data'][0]
        except IndexError:
            # print(f'No flights available for {self.row_data["city"]}')
            pass
        else:
            price = flight['price']
            print(price, self.row_data['city'])
            if price <= self.row_data['lowestPrice']:
                GOOD_DEALS.append(flight)
