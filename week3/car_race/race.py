from copy import deepcopy
from random import randint
import json


class Race:
    def __init__(self, drivers, crash_chance):
        self.drivers = deepcopy(drivers)
        self.crash_chance = crash_chance
        self.drivers_score = []

    def race(self):
        for driver in self.drivers:
            if self.crash_chance * randint(0, 9) > 5:
                self.drivers_score.append((driver, -1))
            else:
                score = driver.car.max_speed * randint(0, 9)
                self.drivers_score.append((driver, score))

        self.drivers_score.sort(key=lambda driver: driver[1])
        return self.drivers_score

    def result(self):
        result = {}
        print_message = ''
        length = len(self.drivers_score)
        for i in range(0, length):
            inx = length - i - 1
            if i == 0 and self.drivers.score[inx][1] != -1:
                result[self.drivers_score[inx]] = 8
                print_message = '{1}{2} - 8\n'.format(print_message, self.drivers_score[inx][0])
            elif i == 1 and self.drivers_score[inx][1] != -1:
                result[self.drivers_score[inx]] = 6
                print_message = '{1}{2} - 6\n'.format(print_message, self.drivers_score[inx][0])
            elif i == 2 and self.drivers_score[inx][1] != -1:
                result[self.drivers_score[inx]] = 4
                print_message = '{1}{2} - 4\n'.format(print_message, self.drivers_score[inx][0])
            elif self.drivers_score[inx][1] != -1:
                result[self.drivers_score[inx]] = 0
            elif self.drivers_score[inx][1] == -1:
                print_message = '{1}Unfortunately, {2} has crashed.\n'.format(print_message, self.drivers.score[inx][0])

            print(print_message)
        return result

    def update_json(self, filename, dict_to_append):
        with open(filename) as json_file:
            data = json.load(json_file)
        data.update(dict_to_append)
        with open(filename, 'w') as json_file:
            json.dump(data, json_file)


