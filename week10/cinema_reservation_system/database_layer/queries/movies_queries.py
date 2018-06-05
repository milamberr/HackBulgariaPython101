INSERT_NEW_MOVIE = """
INSERT INTO movies (name, rating)
    VALUES(%s, %s);
"""

DELETE_MOVIE = """
DELETE
FROM movies
WHERE %s = %s;
"""

SHOW_ALL_MOVIES = """
SELECT id,name,rating
FROM movies
ORDER BY rating;
"""

