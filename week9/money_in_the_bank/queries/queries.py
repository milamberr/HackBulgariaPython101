create_client_table = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(128),
                password VARCHAR(128),
                balance REAL DEFAULT 0,
                message TEXT)'''

update_change_message = """
    UPDATE clients
    SET message = (?)
    WHERE id = (?)
"""

update_change_password = """
UPDATE clients
SET password = (?)
WHERE id = (?)
"""

register_query = "INSERT INTO clients (username, password) VALUES (?, ?)"

login_query1 = """
SELECT id, username, balance, message
FROM clients
"""

login_query2 = """
SELECT id, username, balance, message
FROM clients
WHERE username = (?) AND password = (?)
LIMIT 1
"""
