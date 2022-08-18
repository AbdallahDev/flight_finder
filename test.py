# import requests
#
# end_point = 'https://tequila-api.kiwi.com/v2/search'
#
# params = {
#     'fly_from': 'AMM',
#     'fly_to': 'DOH',
#     'date_from': '17/08/2022',
#     'date_to': '27/09/2022',
#     'return_from': '03/09/2022',
#     'return_to': '03/09/2022',
#     'nights_in_dst_from': 2,
#     'nights_in_dst_to': 2,
#     'flight_type': 'round',
#     'one_for_city': 0,
#     'one_per_date': 0,
#     'adults': 1,
#     'children': 0,
#     'only_working_days': 'false',
#     'only_weekends': 'false',
#     'partner_market': 'us',
#     'curr': 'USD',
#     'locale': 'en',
#     'vehicle_type': 'aircraft',
#     'limit': 500,
# }
#
# headers = {
#     'apikey': "T4vxrX-iACjahtWNkArvRggdEENx2zFk",
#     "accept": "application/json"
# }
#
# req = requests.get(url=end_point, params=params, headers=headers)
# req.raise_for_status()
# data = req.json()
# flights = data['data']
# # flights_data = [{"id":fli} for flight in flights]
# prices = [flight['price'] for flight in flights]
#
# print(min(prices))
# # print(flights)
# import datetime
#
# today_date = datetime.datetime.now().date().strftime("%d/%m/%Y")
# date_1 = datetime.datetime.strptime(today_date, "%d/%m/%Y")
#
# tomorrow_date = date_1 + datetime.timedelta(days=1)
# day_16_date = date_1 + datetime.timedelta(days=16)
#
# print(date_1.strftime("%d/%m/%Y"))
# print(tomorrow_date.strftime("%d/%m/%Y"))
# print(day_16_date.strftime("%d/%m/%Y"))
# print(datetime.datetime.now().date())

# from datetime import datetime
# print(datetime.fromisoformat('2011-11-04'))
#
# print(datetime.fromisoformat('2011-11-04T00:05:23'))
#
# print(datetime.fromisoformat('2011-11-04 00:05:23.283'))
#
# print(datetime.fromisoformat('2011-11-04 00:05:23.283+00:00'))
#
# print(datetime.fromisoformat('2011-11-04T00:05:23+04:00'))
# import datetime
# from datetime import timedelta
#
# delta = timedelta(
#     days=1
# )
# # Only days, seconds, and microseconds remain
# date = datetime.datetime.now().date()
#
# print(date, date - delta)
import datetime

timedelta = datetime.timedelta(days=1)
date_from = datetime.date.today() + timedelta
print(datetime.date.today(), date_from)
