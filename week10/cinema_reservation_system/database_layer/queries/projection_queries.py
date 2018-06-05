INSERT_NEW_PROJECTION = """
INSERT INTO projections (movie_id, type, date, time)
    VALUES(%s, %s, %s, %s);
"""

DELETE_FROM_PROJECTIONS = """
DELETE
FROM projections
WHERE %s = %s;
"""

# SHOW_PROJECTIONS_OF_A_MOVIE = """
# SELECT t.name,t.type,t.date,t.time,
# 100-COUNT(reservations.projection_id) as free_seats
# FROM
#     (SELECT movies.name, projections.type,projections.date,projections.time, projections.id
#         FROM movies
#         JOIN projections
#         ON projections.movie_id=movies.id
#         WHERE movies.id = %s
#     ) as t
# JOIN reservations
# ON reservations.projection_id=t.id
# GROUP BY t.id;
# """
SHOW_PROJECTIONS_OF_A_MOVIE = """
SELECT projections.id,movies.name,projections.type,projections.date,projections.time
FROM movies
JOIN projections
ON movies.id=projections.movie_id
where movies.id = %s
"""