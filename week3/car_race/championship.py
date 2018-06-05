from random import randint
from race import Race


class Championship:
    def __init__(self, name, races_count):
        self.name = name
        self.races_count = races_count
        self.results = []

    def play_races(self, drivers):
        for i in range(self.races_count):
            curr_race = Race(drivers, randint(0, 1))
            curr_race.race()
            self.results.append(curr_race.result())

        return results

    def top3(self):
        for race in self.results:
            for key in race.keys():
                
