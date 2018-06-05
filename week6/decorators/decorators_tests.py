import unittest
from decorators import encrypt, accepts


class DecoratorsTests(unittest.TestCase):
    def test_accept_decorator_works(self):
        with self.subTest('Takes one type as parameter'):
            @accepts(str)
            def take_string(name):
                return name

            self.assertEqual(take_string('Pesho'), 'Pesho')
            with self.assertRaises(TypeError):
                take_string(5)

        with self.subTest('Takes two parameters'):
            @accepts(str, int)
            def take_string_and_int(name, age):
                return name + str(age)

            self.assertEqual(take_string_and_int('Pesho', 5), 'Pesho5')
            with self.assertRaises(TypeError):
                take_string(5, 'name')

        with self.subTest('Takes no parametes'):
            @accepts()
            def dumb_method():
                return 'dumb'

            self.assertEqual(dumb_method(), 'dumb')

    def test_encrypt_decorator_works(self):
        @encrypt(2)
        def get_low(string):
            return string

        self.assertEqual(get_low('Pesho'), 'Rgujq')
        self.assertEqual(get_low('za'), 'bc')

if __name__ == '__main__':
    unittest.main()
