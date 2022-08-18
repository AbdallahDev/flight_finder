import os

import requests as requests

from flight_data import FlightData

SHEET_ENDPOINT = os.environ['SHEET_ENDPOINT']
HEADERS = {"Authorization": "Bearer " + os.environ['SHEET_APIKEY']}


def sheet_data():
    req = requests.get(url=SHEET_ENDPOINT, headers=HEADERS)
    req.raise_for_status()

    data = req.json()
    rows: list = data['prices']

    return rows


class DataManager:
    def __init__(self):
        self.rows = sheet_data()
        self.__store_codes()

    def __store_codes(self):
        rows = self.rows
        flight_data = FlightData()
        for row in rows:
            if row['iataCode'] == "":
                code = flight_data.city_code(city=row['city'])
                body = {"price": {"iataCode": code}}
                req = requests.put(url=SHEET_ENDPOINT + f"/{row['id']}", headers=HEADERS, json=body)
                req.raise_for_status()
