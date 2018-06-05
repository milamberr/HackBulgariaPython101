import hashlib
import sqlite3
from models.client import Client
from queries.queries import *
from utils.utils import strong_pass, accepts


conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    cursor.execute(create_client_table)


def change_message(new_message, logged_user):
    cursor.execute(update_change_message, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    new_hash = hash_pass(logged_user.get_username(), new_pass)
    cursor.execute(update_change_password, (str(new_hash), logged_user.get_id()))
    conn.commit()


def hash_pass(username, password):
    return hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        username.encode(),
        10000
    ).hex()


@strong_pass()
def register(username, password):
    hash = hash_pass(username, password)
    cursor.execute(register_query, (username, str(hash)))
    conn.commit()


def login(username, password):
    hash = hash_pass(username, password)

    cursor.execute(login_query1)
    cursor.execute(login_query2, (username, str(hash)))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False
