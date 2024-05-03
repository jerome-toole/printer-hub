"""Main printer script, run with cron"""

from escpos.printer import Usb, LP
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

# Load environment variables
load_dotenv()

# Set config options from .env file
PRINTER_MODE = os.getenv("PRINTER_MODE", "USB")
LP_PRINTER_NAME = os.getenv("LP_PRINTER_NAME", None)
# TODO: work out the freaky binary/bytes/int thing going on below
USB_PRINTER_VENDOR = os.getenv("USB_PRINTER_VENDOR", 0x0525)  # must be bytes
USB_PRINTER_PRODUCT = os.getenv("USB_PRINTER_PRODUCT", 0xA700)  # def: aures 333
FEED_URL = os.getenv("FEED_URL", None)
PRINTER_WIDTH = int(os.getenv("PRINTER_WIDTH", 500))
LINES_BEFORE = os.getenv("LINES_BEFORE", 0)
LINES_AFTER = os.getenv("LINES_AFTER", 0)
CUT_PAPER = os.getenv("CUT_PAPER").lower() == "true"

# ensure config
# TODO: manage the config way better, maybe with a TUI tool

if PRINTER_MODE.upper() == "LP":
    try:
        printer = LP(LP_PRINTER_NAME)
    except:
        print("Failed to register LP printer. Check LP_PRINTER_NAME env var")
        print(
            "https://python-escpos.readthedocs.io/en/latest/user/usage.html#other-printers"
        )
        exit(1)
elif PRINTER_MODE.upper() == "USB":
    try:

        USB_PRINTER_VENDOR = bytes(USB_PRINTER_VENDOR)
        printer = Usb(USB_PRINTER_VENDOR, USB_PRINTER_PRODUCT, 0)
    except:
        print("Failed to register USB printer. Check 'USB_*' env vars, using lsusb")
        print(
            "https://python-escpos.readthedocs.io/en/latest/user/usage.html#usb-printer"
        )
        exit(1)

try:
    LINES_BEFORE = int(LINES_BEFORE)
    LINES_AFTER = int(LINES_AFTER)
except:
    print("Please ensure that LINES_BEFORE and LINES_AFTER env vars are ints")
    exit(1)

if FEED_URL == None:
    print("No FEED_URL env var set")
    exit(1)

# get content and process

response = requests.get(FEED_URL)
content = BeautifulSoup(response.content, "html.parser").prettify()
printer.text(content)

# actually print

printer.open()

if LINES_BEFORE > 0:
    printer.text("\n" * LINES_BEFORE)

if CUT_PAPER:
    printer.cut()

if LINES_AFTER > 0:
    printer.text("\n" * LINES_AFTER)


printer.close()
