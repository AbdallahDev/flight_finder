import os

import requests as requests

from flight_data import FlightData

ENDPOINT = os.environ['ENDPOINT_SHEETY']
API_KEY = os.environ['APIKEY_SHEETY']
HEADERS = {"Authorization": "Bearer " + API_KEY}


def code_dose_not_exist(code: str) -> bool:
    if code.strip() == "":
        return True

    return False


def new_user():
    f_name = input("Insert Your name: ")
    email = input("Insert Your email: ")

    endpoint = 'https://api.sheety.co/4020d66351458a3fdf604e02fd2d3672/users/emails'
    body = {
        'email': {
            "firstName": f_name,
            "email": email,
        }
    }
    req = requests.post(url=endpoint, json=body)
    req.raise_for_status()


def users() -> list:
    endpoint = 'https://api.sheety.co/4020d66351458a3fdf604e02fd2d3672/users/emails'
    req = requests.get(url=endpoint)
    req.raise_for_status()
    emails = req.json()['emails']
    return emails


class DataManager:
    def __init__(self):
        self.flight_data = FlightData(row_data={})
        self.sheet_rows()

    def sheet_rows(self):
        req = requests.get(url=ENDPOINT, headers=HEADERS)
        req.raise_for_status()
        data = req.json()
        rows: list = data['prices']

        self.loop_rows(data_rows=rows)

    def loop_rows(self, data_rows: list):
        for data_row in data_rows:
            self.flight_data = FlightData(row_data=data_row)

            if code_dose_not_exist(code=data_row['iataCode']):
                code = self.store_code(row_id=data_row['id'])
                data_row.update({'iataCode': code})
                self.flight_data = FlightData(row_data=data_row)

            # here it means the city iataCode is empty
            # So I should get the lowest price flight for that city
            self.flight_data.lowest_price()

    def store_code(self, row_id):
        code = self.flight_data.city_code()
        body = {"price": {"iataCode": code}}
        req = requests.put(url=ENDPOINT + f"/{row_id}", headers=HEADERS, json=body)
        req.raise_for_status()

        return code

    # users data manager

