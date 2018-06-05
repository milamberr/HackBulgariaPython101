from database_layer.models.user import UserModel
from utils.utils import validate_password


class UserController:
    model = UserModel()

    @classmethod
    def user_login(cls, *args):
        return cls.model.user_login(*args)

    @classmethod
    def insert_into_user_table(cls, *args):
        cls.model.insert_into_user_table(*args)

    @classmethod
    @validate_password
    def register_user(cls, *args):
        if not cls.model.username_taken(args[0]):
            cls.model.register_user(*args)
            return True

        return False
