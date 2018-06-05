import unittest
from bill import Bill


class BillTests(unittest.TestCase):
    def setUp(self):

        self.bill = Bill(5)
        self.bill1 = Bill(10)
        self.bill2 = Bill(5)

    def test__int__(self):
        self.assertEqual(int(self.bill), 5)

    def test__str__(self):
        self.assertEqual(str(self.bill), '5')

    def test__eq__equal(self):
        self.assertTrue(self.bill == Bill(5))
        self.assertTrue(self.bill != self.bill1)

    def test__repr__(self):
        self.assertEqual(self.bill.__repr__(), '5')

    def test__hash__(self):
        self.assertEqual(len({self.bill: self.bill, self.bill2: self.bill2}), 1)
        self.assertEqual(len({self.bill: self.bill, self.bill1: self.bill1}), 2)

    def test_negative_amount_raises_value_error(self):
        with self.assertRaises(ValueError):
            int(Bill(-15))

    def test_string_amount_raises_type_error(self):
        with self.assertRaises(TypeError):
            int(Bill('pesho'))


if __name__ == '__main__':
    unittest.main()
