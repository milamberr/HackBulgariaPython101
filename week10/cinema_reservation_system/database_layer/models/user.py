from database_layer.connector import Connector
from database_layer.queries.user_queries import *
from utils.utils import hash_password


class UserModel:
    def __init__(self):
        self.conn = Connector()

    def insert_into_user_table(self, *args):
        self.conn.execute_query(INSERT_NEW_USER, args[0], hash_password(args[0], args[1]))

    def delete_from_user_table(self, *args):
        self.conn.execute_query(DELETE_USER, args[0], hash_password(args[0], args[1]))

    def user_login(self, *args):
        user = self.conn.get_one(USER_LOGIN, args[0], hash_password(args[0], args[1]))
        if user == None:
            return False
        return User(user[0], user[1])

    def register_user(self, *args):
        self.conn.execute_query(INSERT_NEW_USER, args[0], hash_password(args[0], args[1]))

    def username_taken(self, username):
        return self.conn.get_one(USERNAME_TAKEN, username)


class User:
    def __init__(self, id, username):
        self.__id = id
        self.__username = username

    @property
    def id(self):
        return self.__id

    @property
    def username(self):
        return self.__username