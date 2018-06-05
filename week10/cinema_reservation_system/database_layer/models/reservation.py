from database_layer.connector import Connector
from database_layer.queries.reservation_queries import GET_PROJECTION_NUM_FREE_SEATS, GET_PROJECTION_SEATS, INSERT_NEW_RESERVATION

class ReservationModel:
    def __init__(self):
        self.conn = Connector()

    def get_num_free_seats(self, *args):
        seats = self.conn.get_one(GET_PROJECTION_NUM_FREE_SEATS, *args)
        return 100 - seats[0]

    def get_seat_table(self, *args):
        
        seat_table = [
            ['x', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            ['1', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['4', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['5', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['6', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['7', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['8', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['9', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['10', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        ]
        taken_seats = self.conn.get_all(GET_PROJECTION_SEATS, *args)

        for x in taken_seats:
            seat_table[x[0]][x[1]] = 'x'

        return seat_table

    def reserve_a_seat(self, *args):
        new_args = [args[0].id, args[1], args[2], args[3]]
        self.conn.execute_query(INSERT_NEW_RESERVATION, *new_args)
