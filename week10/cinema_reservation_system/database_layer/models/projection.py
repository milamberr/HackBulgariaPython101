from database_layer.connector import Connector
from database_layer.queries.projection_queries import *
from utils.utils import pretty_print


class ProjectionModel:
    def __init__(self):
        self.conn = Connector()

    def show_projections_of_movie(self, *args):
        projections = self.conn.get_all(SHOW_PROJECTIONS_OF_A_MOVIE, *args)
        pretty_print(projections, ['projection_id', 'movie_name', 'type', 'date', 'time'])
        return [Projection(*proj) for proj in projections]


class Projection:
    def __init__(self, projection_id, movie_name, _type, date, time):
        self.projection_id = projection_id
        self.movie_name = movie_name
        self.type = _type
        self.date = date
        self.time = time

    @property
    def id(self):
        return self.projection_id
