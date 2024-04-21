import json
from datetime import datetime, timedelta

import requests
from escpos.printer import Usb

printer = Usb(0x0525, 0xA700)

endpoint = "https://thwopzap.net/api/messages"
headers = {"authorization": "secret123"}
r = requests.get(endpoint, headers=headers)

json = r.json()

for i in json:
    user = i["userName"]
    message = i["text"]
    created_at = datetime.strptime(i["createdAt"], "%Y-%m-%dT%H:%M:%S.%fZ")

    text = f"{user} - {created_at.time()}\n{message}\n\n"
    print(created_at.time(), datetime.now().time())
    # print(created_at < (datetime.now() - timedelta(minutes=8)))

    # printer.text(f"{user} - {created_at}\n{message}\n\n")

# printer.cut()
