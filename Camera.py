import Vechicle
import random
import json

class Camera:
    auto = Vechicle()

    def __init__(self):
        color = ["red", "blue", "green", "yellow", "purple", "orange", "white", "black"]
        a = random.randrange(0,len(color))
        number = "WKZ "+str(random.randrange(1000,10000))
        auto.setVechicle(number,a)

        dict = {"plateNumber": number, "color": color}
        with open("vechicleData.txt", "a") as db:
            json.dump(dict, db, indent=2)


