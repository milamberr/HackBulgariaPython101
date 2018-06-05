import sys
sys.path.insert(0, "../models")
from repair_hour import RepairHour
import sqlite3

class RepairHourController:
    @classmethod
    def list_all_free_hours(cls):
        return RepairHour.list_all_free_hours()

    @classmethod
    def list_all_free_hours_by_date(cls, date):
        return RepairHour.list_all_free_hours_by_date(date)

    @classmethod
    def save_repair_hour(cls, hour_id):
        return RepairHour.save_repair_hour(hour_id)

    @classmethod
    def update_repair_hour(cls, hour_id):
        return RepairHour.update_repair_hour(hour_id)

    @classmethod
    def delete_repair_hour(cls, hour_id):
        return RepairHour.delete_repair_hour(hour_id)
