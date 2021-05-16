import Vechicle
import random

class Camera:
    auto = Vechicle()

    def __init__(self):
        color = ["red", "blue", "green", "yellow", "purple", "orange", "white", "black"]
        a = random.randrange(0,len(color))
        number = "WKZ "+str(random.randrange(1000,10000))
        auto.setVechicle(number,a)


