import sys
import sqlite3
sys.path.insert(0, '../queries')
sys.path.insert(0, '../models')
from user_queries import insert_user
from base_user import BaseUser


class BaseUserController:
    def create_user(self, *args):
        return BaseUser.create_user(*args)