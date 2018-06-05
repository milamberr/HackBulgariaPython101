from database_layer.connector import Connector
from database_layer.queries.create_database_queries import (CREATE_MOVIES_TABLE,
                                                            CREATE_USERS_TABLE,
                                                            CREATE_RESERVATIONS_TABLE,
                                                            CREATE_PROJECTIONS_TABLE)


class DBConnector:
    def __init__(self):
        self.conn = Connector()

    def create_database(self):
        tables = [
            CREATE_MOVIES_TABLE,
            CREATE_USERS_TABLE,
            CREATE_PROJECTIONS_TABLE,
            CREATE_RESERVATIONS_TABLE
        ]

        for table in tables:
            self.conn.execute_query(table)