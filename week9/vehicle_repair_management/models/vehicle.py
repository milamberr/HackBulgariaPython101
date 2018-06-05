import sys
sys.path.insert(0, '../queries')
sys.path.insert(0, '..')
from vehicle_queries import insert_vehicle
import sqlite3


class Vehicle:
    DB_NAME = "vehicle_management.db"
    db = sqlite3.connect(DB_NAME)
    c = db.cursor()

    @classmethod
    def create_vehicle(cls, *args):
        c.execute(insert_vehicle, *args)