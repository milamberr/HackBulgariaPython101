from database_layer.models.movie import MovieModel


class MovieController:
    model = MovieModel()

    @classmethod
    def show_all_movies(cls):
        return cls.model.show_all_movies()

    @classmethod
    def insert_new_movie(cls, *args):
        cls.model.insert_new_movie(*args)
