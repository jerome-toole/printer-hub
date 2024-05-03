"""TESTING MESSAGES IN COMMAND LINE"""

import json
from datetime import datetime, timedelta
import requests
from escpos.printer import Usb

printer = Usb(0x0525, 0xA700)

endpoint = "https://thwopzap.net/api/messages"
headers = {"authorization": "secret123"}
r = requests.get(endpoint, headers=headers)

json = r.json()

logfile_location = "log.txt"

for i in json:
    user = i["userName"]
    message = i["text"]
    created_at = datetime.strptime(i["createdAt"], "%Y-%m-%d %H:%M:%S")

    # 1 Hour to account for daylight savings,
    # 10 minutes for... in the last 10 minutes.
    delta = datetime.now() - timedelta(hours=1, minutes=1)

    is_new = created_at > delta

    if is_new:
        print(f"{user} - {created_at} - {message}")
        text = f"{user} - {created_at.time()}\n{message}\n\n"
        printer.text(f"{user} - {created_at}\n{message}\n\n")
        printer.cut()
