import unittest
from utils import extract_variable_and_power, extract_term


class UtilsTests(unittest.TestCase):
    def test_extract_variable_and_power(self):
        with self.subTest("works with coeff 1"):
            self.assertEqual(extract_variable_and_power('x^2'), ('x', 2))
        with self.subTest('works with coeff > 1'):
            self.assertEqual(extract_variable_and_power('3*x^2'), ('3*x', 2))
        with self.subTest('works with power 1'):
            self.assertEqual(extract_variable_and_power('x'), ('x', 1))

    def test_extract_term(self):
        with self.subTest('work with constant'):
            self.assertEqual(extract_term('2'), (2, None, None))
        with self.subTest('work with coeff > 1'):
            self.assertEqual(extract_term('2*x^3'), (2, 'x', 3))



if __name__ == '__main__':
    unittest.main()
