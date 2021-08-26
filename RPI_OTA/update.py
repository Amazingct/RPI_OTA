import os
import json

ota_dir = "/home/amazing/Documents/RPI_OTA/"

with open("{}config.json".format(ota_dir), "r") as config:
    config = json.load(config)
    print(config)

