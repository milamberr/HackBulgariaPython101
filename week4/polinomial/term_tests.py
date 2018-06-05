import unittest
from term import Term, Polynomial


class TermTests(unittest.TestCase):
    def test_is_constant(self):
        with self.subTest('Term with coeff, variable and power is not'):
            t = Term(coeff=2, variable='x', power=3)

            self.assertFalse(t.is_constant)

        with self.subTest('Constant term is constant'):
            value = 2
            t = Term.constant(value)

            self.assertTrue(t.is_constant)

            self.assertEqual(value, t.coeff)
            self.assertIsNone(t.variable)
            self.assertEqual(0, t.power)

    def test_str_representation_is_correct(self):
        with self.subTest('Term with coeff 1'):
            term = Term(coeff=1, variable='x', power=2)
            self.assertEqual(str(term), 'x^2')

        with self.subTest('Term with power 0'):
            term = Term(coeff=1, variable='x', power=0)
            self.assertEqual(str(term), '1')

        with self.subTest('Term with coeff 0'):
            term = Term(coeff=0, variable='x', power=12)
            self.assertEqual(str(term), '0')

        with self.subTest('Term with coeff bigger than 1 and power 1'):
            term = Term(coeff=2, variable='x', power=1)
            self.assertEqual(str(term), '2*x')

        with self.subTest('Term with coeff 1 and power 1'):
            term = Term(coeff=1, variable='x', power=1)
            self.assertEqual(str(term), 'x')

        with self.subTest('Term with coeff 1 and power bigger than 1'):
            term = Term(coeff=1, variable='x', power=4)
            self.assertEqual(str(term), 'x^4')

        with self.subTest('Term with coeff bigger than 1 and power bigger than 1'):
            term = Term(coeff=2, variable='x', power=3)
            self.assertEqual(str(term), '2*x^3')

    def test_parse_from_string_is_correct(self):
        with self.subTest('Coeff is 0'):
            s = '0'
            self.assertEqual(Term.parse_from_string(s), Term(coeff=0, variable=None, power=0))

        with self.subTest('Coeff is 1'):
            s = 'x^2'
            self.assertEqual(Term.parse_from_string(s), Term(coeff=1, variable='x', power=2))

        with self.subTest('Power is 0'):
            s = '2'
            self.assertEqual(Term.parse_from_string(s), Term(coeff=2, variable=None, power=0))

        with self.subTest('Power is 1'):
            s = '2*x'
            self.assertEqual(Term.parse_from_string(s), Term(coeff=2, variable='x', power=1))

        with self.subTest('Coeff is 1 and power is 1'):
            s = 'x'
            self.assertEqual(Term.parse_from_string(s), Term(coeff=1, variable='x', power=1))

        with self.subTest('Coeff is greater than 1 and power is greater than 1'):
            s = '2*x^2'
            self.assertEqual(Term.parse_from_string(s), Term(coeff=2, variable='x', power=2))

    def test_derivative(self):
        with self.subTest('Derivative of constant is 0'):
            t = Term.constant(2)
            expected = Term.constant(0)

            self.assertEqual(expected, t.derivative())

        with self.subTest('Derivative of 2*x^1'):
            t = Term(coeff=2, variable='x', power=1)
            expected = Term.constant(2)

            self.assertEqual(expected, t.derivative())

        with self.subTest('Derivative of x^1'):
            t = Term(coeff=1, variable='x', power=1)
            expected = Term.constant(1)

            self.assertEqual(expected, t.derivative())

        with self.subTest('Derivative of 2*x^2'):
            t = Term(coeff=2, variable='x', power=2)
            expected = Term(coeff=4, variable='x', power=1)

            self.assertEqual(expected, t.derivative())


class PolynomialTests(unittest.TestCase):
    def test_terms_are_sorted_by_power(self):
        with self.subTest('Two terms with different powers'):
            terms = [
                Term(coeff=1, variable='x', power=2),
                Term(coeff=1, variable='x', power=5)
            ]

            p = Polynomial(terms)

            self.assertEqual(str(p), ('x^5+x^2'))

        with self.subTest('Three terms with two different powers'):
            terms = [
                Term(coeff=1, variable='x', power=2),
                Term(coeff=1, variable='x', power=5),
                Term(coeff=3, variable='x', power=2)
            ]
            p = Polynomial(terms)
            self.assertEqual(str(p), 'x^5+4*x^2')

        with self.subTest('6 different terms'):
            terms = [
                Term(coeff=1, variable='x', power=2),
                Term(coeff=1, variable='x', power=5),
                Term(coeff=3, variable='x', power=3),
                Term(coeff=1, variable='x', power=1),
                Term(coeff=1, variable='x', power=4),
                Term(coeff=3, variable='x', power=0)
            ]
            p = Polynomial(terms)
            self.assertEqual(str(p), 'x^5+x^4+3*x^3+x^2+x+3')

        with self.subTest('Empty'):
            terms = []
            p = Polynomial(terms)
            self.assertEqual(str(p), '')

        with self.subTest('Only with constants'):
            terms = [
                Term(coeff=1, variable='x', power=0),
                Term(coeff=4, variable='x', power=0),
                Term(coeff=3, variable='x', power=0),
                Term(coeff=7, variable='x', power=0),
                Term(coeff=5, variable='x', power=0),
                Term(coeff=3, variable='x', power=0)
            ]
            p = Polynomial(terms)
            self.assertEqual(str(p), '23')

    def test_derivative_works(self):
        with self.subTest('Constant'):
            terms = [
                Term(coeff=1, variable='x', power=0)
            ]
            p = Polynomial(terms).derivative()
            self.assertEqual(str(p), str(Term.constant(0)))

        with self.subTest('Power 1'):
            terms = [
                Term(coeff=1, variable='x', power=1)
            ]
            p = Polynomial(terms).derivative()
            self.assertEqual(str(p), str(Term.constant(1)))

        with self.subTest('Power 2'):
            terms = [
                Term(coeff=1, variable='x', power=2)
            ]
            p = Polynomial(terms).derivative()
            expected = Term(coeff=2, variable='x', power=1)
            self.assertEqual(str(p), str(expected))

        with self.subTest('Two terms'):
            terms = [
                Term(coeff=4, variable='x', power=2),
                Term(coeff=3, variable='x', power=3)
            ]
            p = Polynomial(terms).derivative()
            derived_terms = [
                Term(coeff=8, variable='x', power=1),
                Term(coeff=9, variable='x', power=2)
            ]
            derivative_p = Polynomial(derived_terms)
            self.assertEqual(str(p), str(derivative_p))

        with self.subTest('Three terms'):
            terms = [
                Term(coeff=4, variable='x', power=2),
                Term(coeff=3, variable='x', power=3),
                Term(coeff=3, variable='x', power=0)
            ]
            derived_terms = [
                Term(coeff=8, variable='x', power=1),
                Term(coeff=9, variable='x', power=2),
                Term(coeff=0, variable='x', power=0)
            ]
            p = Polynomial(terms).derivative()
            derived_p = Polynomial(derived_terms)
            self.assertEqual(str(p), str(derived_p))

if __name__ == "__main__":
    unittest.main()
