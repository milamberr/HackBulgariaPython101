CREATE TABLE if not exists
        movies(id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(128),
                rating REAL);

CREATE TABLE if not exists
        users(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(128),
                password VARCHAR(128));

CREATE TABLE if not exists
        projections(id INTEGER PRIMARY KEY AUTOINCREMENT,
                        movie_id INTEGER,
                        type VARCHAR(3),
                        date date,
                        time time,
                        FOREIGN KEY(movie_id) REFERENCES movies(id));

CREATE TABLE if not exists reservations(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                projection_id INTEGER,
                row INTEGER,
                col INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(projection_id) REFERENCES projections(id));
		
		
SELECT t.name,t.type,t.date,t.time,
100-COUNT(reservations.projection_id) as free_seats
FROM
    (SELECT movies.name, projections.type,projections.date,projections.time, projections.id
        FROM movies
        JOIN projections
        ON projections.movie_id=movies.id
        WHERE movies.id =2
    ) as t
JOIN reservations
ON reservations.projection_id=t.id
GROUP BY t.id;

SELECT movies.name, projections.type,projections.date,projections.time, projections.id
        FROM movies
        JOIN projections
        ON projections.movie_id=movies.id
        WHERE movies.id = 2;
