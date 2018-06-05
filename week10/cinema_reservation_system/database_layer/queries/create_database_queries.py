CREATE_MOVIES_TABLE = """
CREATE TABLE if not exists
        movies(id SERIAL PRIMARY KEY,
                name VARCHAR(128),
                rating REAL);

"""

CREATE_USERS_TABLE = """
CREATE TABLE if not exists
        users(id SERIAL PRIMARY KEY,
                username VARCHAR(128),
                password VARCHAR(128));
"""

CREATE_PROJECTIONS_TABLE = """
CREATE TABLE if not exists
        projections(id SERIAL PRIMARY KEY,
                        movie_id INTEGER,
                        type VARCHAR(3),
                        date date,
                        time time,
                        FOREIGN KEY(movie_id) REFERENCES movies(id));
"""

CREATE_RESERVATIONS_TABLE = """
CREATE TABLE if not exists reservations(
                id SERIAL PRIMARY KEY,
                user_id INTEGER,
                projection_id INTEGER,
                row INTEGER,
                col INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(projection_id) REFERENCES projections(id));
"""