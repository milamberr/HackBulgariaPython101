from database_layer.connector import Connector
from database_layer.queries.movies_queries import *
from utils.utils import pretty_print


class MovieModel:
    def __init__(self):
        self.conn = Connector()

    def insert_new_movie(self, *args):
        self.conn.execute_query(INSERT_NEW_MOVIE, *args)

    def delete_movie(self, *args):
        self.cursor.execute_query(DELETE_MOVIE, *args)

    def show_all_movies(self):
        movies = self.conn.get_all(SHOW_ALL_MOVIES)
        pretty_print(movies, ['id', 'name', 'rating'])
        return [Movie(*movie) for movie in movies]

    def show_projections_of_a_movie(self, *args):
        return self.conn.get_all(SHOW_PROJECTIONS_OF_A_MOVIE, *args)


class Movie:
    def __init__(self, id, name, rating):
        self.__id = id
        self.__name = name
        self.__rating = rating

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def rating(self):
        return self.__rating