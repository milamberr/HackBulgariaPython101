from database_layer.models.projection import ProjectionModel


class ProjectionController:
    model = ProjectionModel()

    @classmethod
    def show_projections_of_movie(cls, *args):
        return cls.model.show_projections_of_movie(*args)
