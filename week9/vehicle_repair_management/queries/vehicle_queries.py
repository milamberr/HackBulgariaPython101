insert_vehicle = """
INSERT INTO Vehicle(category, make, model, register_number, gear_box, owner)
VALUES(?, ?, ?, ?, ?, ?)
"""

update_vehicle = """

"""

delete_vehicle = """

"""

list_personal_vehicles = """
SELECT category, make, model, register_number, gear_box, owner
FROM Vehicle
WHERE owner=(?)
"""
