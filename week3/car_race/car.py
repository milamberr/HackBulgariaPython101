class Car:
    def __init__(self, car, model, max_speed):
        self.car = car
        self.model = model
        self.max_speed = max_speed

    def __str__(self):
        return """Car:{0}
                  Model:{1}
                  Max_speed:{2}""".format(self.car, self.model, self.max_speed)

    