from controllers.movie_controller import MovieController
from controllers.projection_controller import ProjectionController
from controllers.reservation_controller import ReservationController
from controllers.user_controller import UserController


class Controller:
    @classmethod
    def insert_new_movie(cls, *args):
        MovieController.insert_new_movie(cls, *args)

    @classmethod
    def insert_new_user(cls, *args):
        UserController.insert_new_user(cls, *args)

    @classmethod
    def insert_new_projection(cls, *args):
        ProjectionController.insert_new_projection(cls, *args)

    @classmethod
    def insert_new_reservation(cls, *args):
        ReservationController.insert_new_reservation(cls, *args)

    @classmethod
    def user_login(cls, *args):
        return UserController.user_login(*args)

    @classmethod
    def user_register(cls, *args):
        return UserController.register_user(*args)

    @classmethod
    def show_all_movies(cls):
        return MovieController.show_all_movies()

    @classmethod
    def show_projections_of_movie(cls, *args):
        return ProjectionController.show_projections_of_movie(*args)

    @classmethod
    def get_num_free_seats(cls, *args):
        return ReservationController.get_num_free_seats(*args)

    @classmethod
    def show_seat_table(cls, *args):
        return ReservationController.show_seat_table(*args)

    @classmethod
    def reserve_a_seat(cls, *args):
        return ReservationController.reserve_a_seat(*args)
