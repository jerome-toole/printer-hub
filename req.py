import json

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

    printer.text(f"{user}: {message}\n")

printer.cut()
