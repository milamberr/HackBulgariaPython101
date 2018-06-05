import sys
from database_layer.models.user import User
from controllers.controller import Controller
from getpass import getpass
from utils.exceptions import PasswordInvalidFormatError
from utils.utils import atomic, pretty_print


options_text = """
---MENU---
1)Log in
2)Register
3)Show movies
4)Show projections of a movie
5)Make reservation
6)Exit
7)Help
"""

helps_text = """
---HELP---
1)Click 1 if you want to login in the system
2)Click 2 if you want to register
3)Click 3 if you want to see all available movies
4)Click 4 if you want to see all projections of a movie.Choose a movie
5)Click 5 if you want to make a reservation.
6)Click 6 if you want to exit the system.
"""


class Menu:
    controller = Controller()

    def start(self):
        self.logged_user = None
        print("Welcome to the cinema reservation system!\n")
        while(True):
            print(options_text)
            option = input("Choose an action:\n")
            if self.logged_user is not None:
                print("You are logged as {0}".format(self.logged_user.username))
            if option == '1':
                self.user_login()
            elif option == '2':
                self.user_register()
            elif option == '3':
                self.show_all_movies()
            elif option == '4':
                self.show_all_projections_of_movie()
            elif option == '5':
                self.make_reservation()
            elif option == '6':
                sys.exit()
            elif option == '7':
                print(helps_text)
            else:
                print("Invalid option\n")

    def user_login(self):
        print("---LOG IN---")
        username = input('Username:')
        password = getpass("Password:")
        logged_user = self.controller.user_login(username, password)
        if logged_user:
            self.logged_user = logged_user
            print("Login successful!")
        else:
            self.logged_username = None
            print("Login failed")

    def user_register(self):
        print("---REGISTRATION---")
        username = input('Username:')
        password = getpass("Password:")
        try:
            if self.controller.user_register(username, password):
                print("Registration successful")
            else:
                print("Username is taken")
        except PasswordInvalidFormatError as exc:
            print(exc)
            print("Registration failed")

    def show_all_movies(self):
        print("---MOVIES---")
        self.controller.show_all_movies()

    def show_all_projections_of_movie(self):
        self.controller.show_all_movies()
        movie_id = input("Choose a movie:")
        self.controller.show_projections_of_movie(movie_id)

    def _user_is_logged(func):
        tmp_menu = """
        1)Log in
        2)Register
        3)Cancel
        """

        def decorated(self, *args):
            if self.logged_user is None:
                while(self.logged_user is None):
                    print(tmp_menu)
                    option = input("Choose option:")
                    if option == '1':
                        self.user_login()
                    elif option == '2':
                        self.user_register()
                    elif option == '3':
                        print("Going back to menu...")
                        return
                    else:
                        print("Invalid option")
            return func(self, *args)
        return decorated

    @atomic
    @_user_is_logged
    def make_reservation(self):
        num_tickets = self.enter_number_of_tickets()
        movie_id = self.choose_a_movie()

        while(True):
            proj_id = self.choose_projection(movie_id)
            if self.controller.get_num_free_seats(proj_id) < num_tickets:
                print("There are not enough free seats on this projection.Please choose a different projection\n")
            else:
                print("Advancing to choosing the seats!")
                break

        reserved_seats = []
        for i in range(num_tickets):
            reserved_seats.append(self.reserve_a_seat(proj_id))

        print("Congratulations!You reserved the following seats.\n")
        pretty_print(reserved_seats, ['row', 'col'])
        print("We wish you a happy cinema!")

    def choose_projection(self, movie_id):
        menu = """
        1)Choose a projection
        2)Cancel reservation
        """

        while(True):
            projections = self.controller.show_projections_of_movie(movie_id)
            print(projections)
            print(menu)
            option = input("Choose option:")
            if option == '1':
                try:
                    projection_id = int(input("Choose projection by id:"))
                    if self.is_valid_id(projection_id, projections):
                        return projection_id
                    else:
                        print("Invalid id\n")
                except Exception:
                    print("Invalid input!\n")
            elif option == '2':
                raise Exception("Canceling reservation...")
            else:
                print('Invalid option\n')

    def enter_number_of_tickets(self):
        menu = """
        1)Choose number of tickets
        2)Cancel reservation
        """

        while(True):
            print(menu)
            option = input("Choose option:")
            if option == '1':
                num_tickets = input("Enter number of tickets:")
                try:
                    num_tickets = int(num_tickets)
                    return num_tickets
                except Exception:
                    print("Invalid number tickets\n")
            elif option == '2':
                raise Exception("Canceling reservation...")

    def is_valid_id(self, id, data):
        for obj in data:
            if obj.id == id:
                return True
        return False

    def choose_a_movie(self):
        menu = """
        1)Choose a movie
        2)Cancel reservation
        """
        while(True):
            movies = self.controller.show_all_movies()
            print(menu)
            option = input("Choose option:")
            if option == '1':
                try:
                    movie_id = input("Choose a movie by id:")
                    movie_id = int(movie_id)
                    if self.is_valid_id(movie_id, movies):
                        return movie_id
                    else:
                        print("Invalid id\n")
                except Exception:
                    print("Invalid movie id!\n")
            elif option == '2':
                raise Exception("Canceling reservation...")
            else:
                print("Invalid option\n")

    def reserve_a_seat(self, projection_id):
        self.controller.show_seat_table(projection_id)
        menu = """
        1)Choose a seat
        2)Cancel
        """
        while(True):
            print(menu)
            option = input("Choose option:")
            if option == '1':
                row = input("Choose row:")
                col = input("Choose col:")

                if self.controller.reserve_a_seat(self.logged_user, projection_id, row, col):
                    print("Reserved seat {0}-{1} successfuly!".format(row, col))
                    break
                else:
                    continue
            elif option == '2':
                raise Exception("Canceling reservation...")
            else:
                print("Invalid option!\n")
