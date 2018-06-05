import unittest
from fractions import gcd, simplify_fraction, collect_fractions, compare_fractions


class Week2Tests(unittest.TestCase):
    def test_gcd_works(self):
        self.assertEqual(gcd(1, 1), 1)
        self.assertEqual(gcd(15, 1), 1)
        self.assertEqual(gcd(7, 11), 1)
        self.assertEqual(gcd(12, 8), 4)

    def test_gcd_input_error(self):
        with self.assertRaises(TypeError):
            gcd('a', 0)
        with self.assertRaises(TypeError):
            gcd(0, 'a')
        with self.assertRaises(TypeError):
            gcd('a', 'a')

    def test_simplify_fraction_works(self):
        self.assertEqual(simplify_fraction((3, 9)), (1, 3))
        self.assertEqual(simplify_fraction((1, 7)), (1, 7))
        self.assertEqual(simplify_fraction((4, 10)), (2, 5))
        self.assertEqual(simplify_fraction((63, 462)), (3, 22))

    def test_simplify_fraction_correct_input(self):
        with self.assertRaises(TypeError):
            simplify_fraction(('a', 1))
        with self.assertRaises(TypeError):
            simplify_fraction((1, 'a'))
        with self.assertRaises(TypeError):
            simplify_fraction(('a', 'a'))

    def test_simplify_fraction_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            simplify_fraction((1, 0))

    def test_collect_fractions_works(self):
        self.assertEqual(collect_fractions([(1, 4), (1, 2)]), (3, 4))
        self.assertEqual(collect_fractions([(1, 7), (2, 6)]), (10, 21))

    def test_collect_fractions_correct_input(self):
        with self.assertRaises(TypeError):
            collect_fractions('a_string')
        with self.assertRaises(TypeError):
            collect_fractions(['', (1, 2)])
        with self.assertRaises(TypeError):
            collect_fractions([(1, 2), {1: 'b'}])
        with self.assertRaises(TypeError):
            collect_fractions([(1, ''), (1, 2)])

    def test_collect_fractions_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            collect_fractions([(1, 0), (1, 2)])

    def test_compare_fractions_works(self):
        self.assertEqual(compare_fractions((1, 2), (2, 3)), False)
        self.assertEqual(compare_fractions((7, 8), (1, 5)), True)

    def test_compare_fractions_correct_input(self):
        with self.assertRaises(ValueError):
            compare_fractions((' ', 5), (4, ' '))
        with self.assertRaises(ValueError):
            compare_fractions((5, ' '), (' ', 2))


if __name__ == '__main__':
    unittest.main()
