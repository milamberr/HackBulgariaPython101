INSERT_NEW_USER = """
INSERT INTO users (username, password)
    VALUES(%s, %s);
"""

DELETE_USER = """
DELETE
FROM users
WHERE %s = %s;
"""

USER_LOGIN = """
SELECT *
FROM users
WHERE username = %s AND password = %s;
"""

USERNAME_TAKEN = """
SELECT *
FROM users
WHERE username = %s
"""
