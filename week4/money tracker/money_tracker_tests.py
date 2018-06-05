import unittest
from money_tracker import MoneyTracker
from category import Category, Expense, Income
from aggregated_money_tracker import AggregateData


class MoneyTrackerTests(unittest.TestCase):
    def setUp(self):
        self.categories = [Income('760', 'Salary'),
                           Expense('5.5', 'Eating Out'),
                           Expense('34', 'Clothes'),
                           Income('50', 'Savings')]
        self.strings = ['760, Salary, New Income',
                        '5.5, Eating Out, New Expense',
                        '34, Clothes, New Expense',
                        '50, Savings, New Income']

        self.strings1 = ['50, Savings, New Income',
                         '15, Food, New Expense',
                         '200, Deposit, New Income',
                         '5, Sports, New Expense']

        self.categories1 = [Income('50', 'Savings'),
                            Expense('15', 'Food'),
                            Income('200', 'Deposit'),
                            Expense('5', 'Sports')]
        self.aggregator1 = AggregateData({'=== 22-03-2018 ===': self.strings, '=== 23-03-2018 ===': self.strings1})
        self.tracker1 = MoneyTracker(self.aggregator1)

    def test_list_user_expenses_ordered_by_categories(self):
        result = [
            self.categories[2],
            self.categories[1],
            self.categories1[1],
            self.categories1[3]
        ]
        self.assertEqual(self.tracker1.list_user_expenses_ordered_by_categories(), result)

    def test_list_income_categories(self):
        result = [
            self.categories[0],
            self.categories[3],
            self.categories1[0],
            self.categories1[2]
        ]
        self.assertEqual(self.tracker1.list_income_categories(), result)

    def test_list_expense(self):
        result = [
            self.categories[1],
            self.categories[2],
            self.categories1[1],
            self.categories1[3]
        ]
        self.assertEqual(self.tracker1.list_expense_categories(), result)

    def test_add_income(self):
        with self.subTest("with new date"):
            data = self.tracker1.list_user_data()
            self.tracker1.add_income("Stipendiq", 100, '22-03-2018')
            self.assertTrue(
                Income(100, "Stipendiq") in data['=== 22-03-2018 ===']
            )

        with self.subTest("with old date"):
            data = self.tracker1.list_user_data()
            self.tracker1.add_expense("Tototo", 1.5, '22-03-2018')
            self.assertTrue(
                Income(1.5, "Tototo") in data['=== 22-03-2018 ===']
            )

    def test_add_expense(self):
        with self.subTest("with new date"):
            data = self.tracker1.list_user_data()
            self.tracker1.add_expense("Kniga", 17, '22-03-9999')
            self.assertTrue(
                Expense(17, "Kniga") in data['=== 22-03-9999 ===']
            )

        with self.subTest("with old date"):
            data = self.tracker1.list_user_data()
            self.tracker1.add_expense("Kola", 155.5, '22-03-2018')
            self.assertTrue(
                Expense(155.5, "Kola") in data['=== 22-03-2018 ===']
            )


if __name__ == '__main__':
    unittest.main()
