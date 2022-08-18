import datetime
from datetime import timedelta
import os

import requests

# from data_manager import DataManager

# /locations/query
FLIGHT_ENDPOINT = os.environ['FLIGHT_ENDPOINT']
SEARCH_ENDPOINT = '/v2/search'
HEADERS = {"accept": "application/json", "apikey": os.environ['FLIGHT_APIKEY']}
LOCALE = 'en-US'
LOCATION_TYPES = 'city'
LIMIT = 1


class FlightData:
    def __init__(self):
        self.__params = {
            'locale': LOCALE,
            'location_types': LOCATION_TYPES,
            'limit': LIMIT, }

    def city_code(self, city: str) -> str:
        self.__params.update({'term': city})
        req = requests.get(url=FLIGHT_ENDPOINT,
                           headers=HEADERS, params=self.__params)
        req.raise_for_status()
        # the datatype of data variable is dict
        data = req.json()
        code = data['locations'][0]['code']

        return code

    def lowest_price(self, rows: list):
        end_point = 'https://tequila-api.kiwi.com/v2/search'

        params = {
            'fly_from': 'AMM',
            'fly_to': 'DOH',
            'date_from': '17/08/2022',
            'date_to': '27/09/2022',
            'return_from': '03/09/2022',
            'return_to': '03/09/2022',
            'nights_in_dst_from': 2,
            'nights_in_dst_to': 2,
            'flight_type': 'round',
            'one_for_city': 0,
            'one_per_date': 0,
            'adults': 1,
            'children': 0,
            'only_working_days': 'false',
            'only_weekends': 'false',
            'partner_market': 'us',
            'curr': 'USD',
            'locale': 'en',
            'vehicle_type': 'aircraft',
            'limit': 500,
        }

        headers = {
            'apikey': "T4vxrX-iACjahtWNkArvRggdEENx2zFk",
            "accept": "application/json"
        }
        codes = [row['iataCode'] for row in rows]
        for code in codes:
            params['fly_to'] = code
            params['date_from'] = datetime.date.today() + datetime.timedelta(days=1)
            params['return_from'] = datetime.date.today() + datetime.timedelta(weeks=4)
            params['return_to'] = datetime.date.today() + datetime.timedelta(weeks=4)
            req = requests.get(
                url=end_point,
                params=params,
                headers=headers
            )
            data = req.json()
            prices = [flight['price'] for flight in data['data']]
            min_price = min(prices)
            # if min_price <= ro
            print(f"min price: {min_price}")
