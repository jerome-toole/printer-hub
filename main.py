from escpos.printer import Usb, LP
import os
from dotenv import load_dotenv
import images
import web_content

# Load environment variables
load_dotenv()

# Set options from .env file
LP_PRINTER_NAME = os.getenv("LP_PRINTER_NAME")
USB_PRINTER_VENDOR = os.getenv("USB_PRINTER_VENDOR", "0x0525")
USB_PRINTER_PRODUCT = os.getenv("USB_PRINTER_PRODUCT", "0xa700")
PRINTER_WIDTH = int(os.getenv("PRINTER_WIDTH", 500))

# Create printer object
if LP_PRINTER_NAME:
    printer = LP(LP_PRINTER_NAME)
else:
    # Default to a common USB printer if no name is provided
    # You would need to set the correct vendor and product IDs for your specific printer
    printer = Usb(USB_PRINTER_VENDOR, USB_PRINTER_PRODUCT, 0)

# Set up print items
# img_file = "/Users/jerometoole/Desktop/fax/ed-josh.jpg"
img_file = None
txtURL = "https://thwopzap.net/"

printer.open()

if int(os.getenv("SPACE_BEFORE", False)):
    printer.text(os.getenv("SPACE_BEFORE"))


# Print Content

if txtURL:
    content = web_content.get_web_content(txtURL, 5)

    printer.text(content)

if img_file:
    img_file = images.prepare_image(img_file, PRINTER_WIDTH)

    # Print the image
    printer.image(img_file)


# Finish printing

if int(os.getenv("SPACE_AFTER", False)):
    printer.text(os.getenv("SPACE_AFTER"))


# printer.cut()
printer.close()
