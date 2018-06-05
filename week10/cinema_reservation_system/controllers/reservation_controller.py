from database_layer.models.reservation import ReservationModel
from utils.utils import validate_seat
from pprint import pprint


class ReservationController:
    model = ReservationModel()

    @classmethod
    def get_num_free_seats(cls, *args):
        return cls.model.get_num_free_seats(*args)

    @classmethod
    def show_seat_table(cls, *args):
        seat_table = cls.model.get_seat_table(*args)
        pprint(seat_table)

    @classmethod
    @validate_seat
    def reserve_a_seat(cls, user, projection_id, row, col):
        seat_table = cls.model.get_seat_table(projection_id)
        if seat_table[row][col] == '.':
            cls.model.reserve_a_seat(user, projection_id, row, col)
            return True
        else:
            print('This seat is taken!')
