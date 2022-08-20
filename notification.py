import os
import smtplib
import ssl

from flight_data import GOOD_DEALS


def notify():
    body: str = make_body()

    smtp_server = os.environ['SMTP_SERVER']
    port = 587
    sender_addrs = os.environ['SENDER_ADDRS']
    receiver_addrs = sender_addrs
    password = os.environ['SENDER_PASSWORD']
    message = f"""\
    Subject: Flights

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
            body += "Flight details:\n\n"
            for info in deal.items():
                body += f"- {info[0]}: {info[1]}\n"
            body += "\n\n"
    else:
        body = 'There isn\'t good deals for today'

    return body


class Notification:
    def __init__(self):
        notify()
