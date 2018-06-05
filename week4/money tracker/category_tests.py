import unittest
from category import Category, Expense, Income


class CategoryTests(unittest.TestCase):
    def setUp(self):
        self.income = Income('500', 'hrana')

    def test_repr(self):
        self.assertEqual(self.income.__repr__(), "Amount:500\nCategory:hrana")

if __name__ == '__main__':
    unittest.main()