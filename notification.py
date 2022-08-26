import os
import smtplib
import ssl

from flight_data import GOOD_DEALS
from data_manager import users


def notify():
    users_list = users()
    for user in users_list:
        body: str = make_body()

        smtp_server = os.environ['SMTP_SERVER']
        port = 587
        sender_addrs = os.environ['SENDER_ADDRS']
        receiver_addrs = user['email']
        password = os.environ['SENDER_PASSWORD']
        message = f"""\
        Subject: Flights
    
    
        Hi {user['firstName']}
        {body}"""

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(user=sender_addrs, password=password)
            server.sendmail(from_addr=sender_addrs, to_addrs=receiver_addrs, msg=message)


def make_body() -> str:
    body: str = ""

    if len(GOOD_DEALS) > 0:
        for deal in GOOD_DEALS:
            body += f"Flight {GOOD_DEALS.index(deal) + 1}:\n\n"
            body += f"- City From: {deal['cityFrom']}\n"
            body += f"- City To: {deal['cityTo']}\n"
            body += f"- Price: {deal['price']}\n"
            body += "\n\n"
    else:
        body = 'There isn\'t good deals for today'

    return body


class Notification:
    def __init__(self):
        notify()
