import unittest
import os
import sql_manager
import hashlib
from utils.exceptions import PasswordIncludesUsernameError, PasswordTooShortError, PasswordRequiredCharsMissingError


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.register('Petur', 'Parolata#123')

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')

    @classmethod
    def tearDownClass(cls):
        os.remove("bank.db")

    def test_register(self):
        sql_manager.register('Petur', 'Parolata#1234')

        hash = sql_manager.hash_pass('Petur', 'Parolata#1234')

        sql_manager.cursor.execute('SELECT Count(*)  FROM clients WHERE username = (?) AND password = (?)', ('Petur', str(hash)))
        users_count = sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = sql_manager.login('Petur', 'Parolata#123')
        self.assertEqual(logged_user.get_username(), 'Petur')

    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Petur', 'Parolata#')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = sql_manager.login('Petur', 'Parolata#123')
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = sql_manager.login('Petur', 'Parolata#123')
        new_password = "NovataParola#23"
        sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = sql_manager.login('Petur', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Petur')

    def test_sql_injection_protection(self):
        with self.subTest('\' OR 1 = 1 --'):
            logged_user = sql_manager.login('\' OR 1 = 1 --', 'test_protection')
            self.assertFalse(logged_user)

        with self.subTest('" or ""="'):
            logged_user = sql_manager.login('" or ""="', '" or ""="')
            self.assertFalse(logged_user)

        with self.subTest('105; DROP TABLE clients'):
            sql_manager.login('105; DROP TABLE clients', '--')
            user = sql_manager.login('Petur', 'Parolata#123')
            self.assertEqual(user.get_username(), 'Petur')

    def test_decorator_strong_pass_when_register(self):
        with self.subTest('Password not long enough'):
            with self.assertRaises(PasswordTooShortError):
                sql_manager.register('Petur', '123')

        with self.subTest('Password doesnt have capital letter'):
            with self.assertRaises(PasswordRequiredCharsMissingError):
                sql_manager.register('Petur', 'Parolata23')

            with self.assertRaises(PasswordRequiredCharsMissingError):
                sql_manager.register('Petur', 'parolata#23')

            with self.assertRaises(PasswordRequiredCharsMissingError):
                sql_manager.register('Petur', 'Parolata#')

        with self.subTest('Password includes username as a substring'):
            with self.assertRaises(PasswordIncludesUsernameError):
                sql_manager.register('Petur', 'pPetur#2123')





if __name__ == '__main__':
    unittest.main()
