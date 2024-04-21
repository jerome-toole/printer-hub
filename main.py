from escpos import config

CONFIG_LOCATION = "/home/joshmurr/.config/python-escpos"
c = config.Config()
c.load(CONFIG_LOCATION)

printer = c.printer()
printer.open()
printer.image("./cow.jpg")
printer.cut()

# image(
#     img_source,
#     high_density_vertical=True,
#     high_density_horizontal=True,
#     impl="bitImageRaster",
#     fragment_height=960,
#     center=False,
# )

# printer.profile.profile_data["media"]["width"]["pixel"] = 128
# import random
# MIN = 4000000000001
# MAX = 4999999999999
#
# for i in range(18):
#     code = random.randint(MIN, MAX)
#     printer.barcode(f"{code}", "EAN13", 255, 5, "OFF", "")
