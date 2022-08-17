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
        codes = [row['iataCode'] for row in rows]
        for code in codes:
            req = requests.get(
                url='https://tequila-api.kiwi.com/v2/search',
                params=self.__params,
                headers=HEADERS
            )
