INSERT_NEW_RESERVATION = """
INSERT INTO reservations (user_id, projection_id, row, col)
    VALUES(%s, %s, %s, %s);
"""

DELETE_RESERVATION = """
DELETE
FROM reservations
WHERE %s = %s;
"""

GET_PROJECTION_NUM_FREE_SEATS = """
SELECT COUNT(*)
FROM reservations
WHERE projection_id = %s
"""

GET_PROJECTION_SEATS = """
SELECT row, col
FROM reservations
WHERE projection_id = %s
"""