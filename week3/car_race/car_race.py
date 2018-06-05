import json
from car import car
from driver import driver
from race import race


def read_json(filename):
    if type(filename) is not str or '.json' not in filename:
        raise TypeError
    with open(filename) as f:
        data = json.load(f)
    return data


def main():
    data = read_json('cars.json')


if __name__ == '__main__':
    main()
