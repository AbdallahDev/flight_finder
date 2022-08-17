from data_manager import DataManager
from flight_data import FlightData

data_manager = DataManager()

flight_data = FlightData()
flight_data.lowest_price(rows=data_manager.rows)
