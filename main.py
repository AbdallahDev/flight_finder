from data_manager import DataManager, new_user
from notification import Notification

data_manager = DataManager()

notification = Notification()

insert_user = input("Do you want to add a new user? y/n: ").lower()
if insert_user == 'y':
    new_user()
