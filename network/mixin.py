'''
mixin
'''
class CarMinIn:
    def ready(self):
        print("mixin ready")
    def start(self):
        print("{} {}".format(self.name, self.speed))

class Performance:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.ready()

class SuperCar(CarMinIn, Performance):
    def show_info(self):
        print("{} {}".format(self.name, self.speed))
    def start(self):
        print("start")

s = SuperCar("car", 300)
s.show_info()
s.start()