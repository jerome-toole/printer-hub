from escpos.printer import Usb

// TODO: check why this is this way again :/
printer = Usb(0x0525,0xa700,0)

printer.open()

printer.text("hey, worl")

printer.cut()
