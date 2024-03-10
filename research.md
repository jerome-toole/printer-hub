## Links
- https://learn.adafruit.com/mini-thermal-receipt-printer/making-connections
- https://github.com/andoncemore/sirius?tab=readme-ov-file
- https://mike42.me/blog/2014-10-26-setting-up-an-epson-receipt-printer
- https://mike42.me/blog/2015-03-getting-a-usb-receipt-printer-working-on-linux
- https://github.com/song940/node-escpos

## Hardware
- LP2824+ Zebra Printer


## Hub

- Basic HTTP Authentication
- Receive POST request from the client (CLI script, Web form, etc.) and return a 200 OK response
- Saves the message to the database
- Queryable by the bridge via GET request

## Bridge
- Polls the hub for new messages every x seconds (CURL GET request)
- Prints new messages to the printer in the correct format


### Authentication
Just a standard API key gets sent with the POST request.
