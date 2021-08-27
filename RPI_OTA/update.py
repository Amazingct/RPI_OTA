import json
import os
import time

wait = 0
os.chdir("/home/pi/RPI_OTA")

with open("config.json", "r") as config:
    config = json.load(config)
    os.chdir(config["ota_dir"])
    # wait
    time.sleep(wait)
    # download
    try:
        os.system("git clone {}".format(config["link"]))
        os.system("sudo rm -r {}".format(config["project_dir"]+config["project_name"]))
        os.system("mv {} {}".format(config["project_name"], config["project_dir"]))

    except Exception as e:
        print(e)
        os.system("sudo rm -r {}".format(config["ota_dir"] + config["project_name"]))

    time.sleep(5)
# Ensure the program dose not update until next boot
#while True:
#    pass
