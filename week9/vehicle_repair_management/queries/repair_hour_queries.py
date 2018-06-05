insert_repair_hour = """
INSERT INTO RepairHour(date, start_hour, vehicle, bill, mechanic_service)
VALUES(?, ?, ?, ?, ?)
"""

list_all_free_hours = """
SELECT date, start hour
FROM RepairHour
WHERE vehicle is null;
"""

list_all_hours_by_date = """
SELECT date,start hour
from RepairHour
WHERE date like (?)
"""
