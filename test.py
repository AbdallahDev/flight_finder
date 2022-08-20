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
# import datetime
#
# timedelta = datetime.timedelta(days=1)
# date_from = datetime.date.today() + timedelta
# print(datetime.date.today(), date_from)

# dic1 = {'key': 'value'}
# if len(dic1) == 0:
#     print('empty')
#     print(len(dic1))
# else:
#     print('filled')
#     print(len(dic1))

dict1 = {
    'id': '10db1db84b1d4b4398109b1a_0|10db1db84b1d4b4398109b1a_1|10db1db84b1d4b4398109b1a_2|10db1db84b1d4b4398109b1a_3',
    'flyFrom': 'AMM', 'flyTo': 'SAW', 'cityFrom': 'Amman', 'cityCodeFrom': 'AMM', 'cityTo': 'Istanbul',
    'cityCodeTo': 'IST', 'countryFrom': {'code': 'JO', 'name': 'Jordan'}, 'countryTo': {'code': 'TR', 'name': 'Turkey'},
    'nightsInDest': 38, 'quality': 472.046626, 'distance': 1183.52,
    'duration': {'departure': 15600, 'return': 15900, 'total': 31500}, 'price': 269,
    'conversion': {'EUR': 378.046861, 'JOD': 269}, 'fare': {'adults': 269, 'children': 269, 'infants': 269},
    'price_dropdown': {'base_fare': 269, 'fees': 0}, 'bags_price': {'1': 0},
    'baglimit': {'hand_height': 40, 'hand_length': 55, 'hand_weight': 8, 'hand_width': 23, 'hold_dimensions_sum': 158,
                 'hold_height': 52, 'hold_length': 78, 'hold_weight': 15, 'hold_width': 28, 'personal_item_height': 30,
                 'personal_item_length': 40, 'personal_item_weight': 4, 'personal_item_width': 15},
    'availability': {'seats': 1}, 'airlines': ['TK'], 'route': [
        {'id': '10db1db84b1d4b4398109b1a_0', 'combination_id': '10db1db84b1d4b4398109b1a', 'flyFrom': 'AMM',
         'flyTo': 'DLM', 'cityFrom': 'Amman', 'cityCodeFrom': 'AMM', 'cityTo': 'Dalaman', 'cityCodeTo': 'DLM',
         'airline': 'TK', 'flight_no': 7941, 'operating_carrier': 'TK', 'operating_flight_no': '7941',
         'fare_basis': 'LYDAJRR', 'fare_category': 'M', 'fare_classes': 'L', 'fare_family': '', 'return': 0,
         'bags_recheck_required': False, 'vi_connection': False, 'guarantee': False, 'equipment': None,
         'vehicle_type': 'aircraft', 'local_arrival': '2022-08-25T19:10:00.000Z',
         'utc_arrival': '2022-08-25T16:10:00.000Z', 'local_departure': '2022-08-25T17:20:00.000Z',
         'utc_departure': '2022-08-25T14:20:00.000Z'},
        {'id': '10db1db84b1d4b4398109b1a_1', 'combination_id': '10db1db84b1d4b4398109b1a', 'flyFrom': 'DLM',
         'flyTo': 'SAW', 'cityFrom': 'Dalaman', 'cityCodeFrom': 'DLM', 'cityTo': 'Istanbul', 'cityCodeTo': 'IST',
         'airline': 'TK', 'flight_no': 7453, 'operating_carrier': 'TK', 'operating_flight_no': '7453',
         'fare_basis': 'LYDAJRR', 'fare_category': 'M', 'fare_classes': 'Y', 'fare_family': '', 'return': 0,
         'bags_recheck_required': False, 'vi_connection': False, 'guarantee': False, 'equipment': None,
         'vehicle_type': 'aircraft', 'local_arrival': '2022-08-25T21:40:00.000Z',
         'utc_arrival': '2022-08-25T18:40:00.000Z', 'local_departure': '2022-08-25T20:25:00.000Z',
         'utc_departure': '2022-08-25T17:25:00.000Z'},
        {'id': '10db1db84b1d4b4398109b1a_2', 'combination_id': '10db1db84b1d4b4398109b1a', 'flyFrom': 'SAW',
         'flyTo': 'ESB', 'cityFrom': 'Istanbul', 'cityCodeFrom': 'IST', 'cityTo': 'Ankara', 'cityCodeTo': 'ANK',
         'airline': 'TK', 'flight_no': 7254, 'operating_carrier': 'TK', 'operating_flight_no': '7254',
         'fare_basis': 'VYEAJRR', 'fare_category': 'M', 'fare_classes': 'Y', 'fare_family': '', 'return': 1,
         'bags_recheck_required': False, 'vi_connection': False, 'guarantee': False, 'equipment': None,
         'vehicle_type': 'aircraft', 'local_arrival': '2022-10-02T22:45:00.000Z',
         'utc_arrival': '2022-10-02T19:45:00.000Z', 'local_departure': '2022-10-02T21:45:00.000Z',
         'utc_departure': '2022-10-02T18:45:00.000Z'},
        {'id': '10db1db84b1d4b4398109b1a_3', 'combination_id': '10db1db84b1d4b4398109b1a', 'flyFrom': 'ESB',
         'flyTo': 'AMM', 'cityFrom': 'Ankara', 'cityCodeFrom': 'ANK', 'cityTo': 'Amman', 'cityCodeTo': 'AMM',
         'airline': 'TK', 'flight_no': 7966, 'operating_carrier': 'TK', 'operating_flight_no': '7966',
         'fare_basis': 'VYEAJRR', 'fare_category': 'M', 'fare_classes': 'V', 'fare_family': '', 'return': 1,
         'bags_recheck_required': False, 'vi_connection': False, 'guarantee': False, 'equipment': None,
         'vehicle_type': 'aircraft', 'local_arrival': '2022-10-03T02:10:00.000Z',
         'utc_arrival': '2022-10-02T23:10:00.000Z', 'local_departure': '2022-10-02T23:55:00.000Z',
         'utc_departure': '2022-10-02T20:55:00.000Z'}],
    'booking_token': 'El2Z7cly7-P0y7TxDZJGtc6xIaLt_lvXeYoOit2-bdhN4VhQ33eUICJ-_xd6WEgybRBlwA_0OoqtFtq73y6CKcS-O7Wgzop7UGbXvMNY1crUUDopzwpYAWQf_u3cb_8Kn26VhrOviHHA6kmDx6HRgqUnnjyi9uM43eVZxB3iI1UkxdldMRyr-RV0WzjtKL93DNEfhWW8UQC5bm0oTBQil6wn7TH8MWn1ZhHeyO-i0RRVk8MZupgxJmR50FpB1T17mhU2FGWtKr0Rlxa4OWAEEAzYmzot-a9-Rf41-MudI2daBNfzYtmEB2s94lNgIZalvPS6ipRJwwiuC1FpGQVZi4BA5gOQpITZ_dxC_C4yvtoWUB5Qta163-SMXQEpdIDXmQzKuR2jqZh1Tg7fzJaA4rZyuy-_SLbDAjy450YOrvwlHdEkATCfrtqbkrTd4fMDsG7NfL25Ru6dNXXjrbK3skH3pHEDM7W3SWWPqJqn3qIw=',
    'facilitated_booking_available': True, 'pnr_count': 1, 'has_airport_change': False, 'technical_stops': 0,
    'throw_away_ticketing': False, 'hidden_city_ticketing': False, 'virtual_interlining': False,
    'local_arrival': '2022-08-25T21:40:00.000Z', 'utc_arrival': '2022-08-25T18:40:00.000Z',
    'local_departure': '2022-08-25T17:20:00.000Z', 'utc_departure': '2022-08-25T14:20:00.000Z'}

body: str = ""
for item in dict1.items():
    body += str(item) + "\n"

body += "\n\n"
print(f"subject: flight \n\n {body}")
print(f"subject: flight \n\n {body}")
