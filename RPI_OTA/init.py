import os
import json


with open("config.json", "r") as config:
    config = json.load(config)
    with open("project.service", "r") as service:
        text = service.read()
        for program in config["autostart"]:
            service=text.replace('*project_program*', config["project_dir"]+program).replace("*exec*", config["exec"])
            print("____________________")
            open(program[:-3]+".service","w").write(service)
            print("run this:", "sudo mv {}{} /lib/systemd/system/".format(config["ota_dir"],program[:-3]+".service"))
            print("run this:", "sudo chmod 644 /lib/systemd/system/{}".format(program[:-3]+".service"))
            print("run this:", "sudo systemctl daemon-reload")
            print("sudo systemctl enable {}".format(program[:-3] + ".service"))



