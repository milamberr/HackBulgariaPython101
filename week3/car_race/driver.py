from car import Car


class Driver:
    def __init__(self, name, car):
        self.name = name
        self.car = car

    def __str__(self):
        return """Driver name:{0}
                  Car:{1}""".format(self.name, str(self.car))
