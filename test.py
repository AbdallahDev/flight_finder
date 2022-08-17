import requests

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

req = requests.get(url=end_point, params=params, headers=headers)
req.raise_for_status()
data = req.json()
flights = data['data']
# flights_data = [{"id":fli} for flight in flights]
prices = [flight['price'] for flight in flights]

print(min(prices))
# print(flights)
