import psycopg2
from database_layer.settings import DB_NAME, USER


class Connector:
    def __init__(self):
        db_conn = 'dbname={0} user={1}'.format(DB_NAME, USER)
        self.conn = psycopg2.connect(db_conn)
        self.cursor = self.conn.cursor()

    def execute_query(self, query, *args):
        self.cursor.execute(query, (*args, ))
        self.conn.commit()

    def get_one(self, query, *args):
        self.cursor.execute(query, (*args, ))
        return self.cursor.fetchone()

    def get_all(self, query, *args):
        self.cursor.execute(query, (*args, ))
        return self.cursor.fetchall()
