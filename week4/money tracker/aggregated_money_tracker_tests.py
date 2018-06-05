import unittest
from aggregated_money_tracker import AggregateData
from category import Expense, Income, Category


class AggregateDataTests(unittest.TestCase):
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
        self.aggregator = AggregateData({'=== 22-03-2018 ===': self.strings})
        self.aggregator1 = AggregateData({'=== 22-03-2018 ===': self.strings, '=== 23-03-2018 ===': self.strings1})

    def test_aggregate_object_works_with_income(self):
        self.assertEqual(AggregateData.aggregate_object(self.strings[0]), self.categories[0])

    def test_aggregate_object_works_with_expense(self):
        self.assertEqual(AggregateData.aggregate_object(self.strings[1]), self.categories[1])

    def test_aggregate_data_in_a_date(self):
        self.assertEqual(AggregateData.aggregate_data_in_a_date(self.strings), self.categories)

    def test_aggregate_data_in_a_date_with_empty(self):
        self.assertEqual(AggregateData.aggregate_data_in_a_date([]), [])

    def test_aggregate_data_with_one_date(self):
        result = self.aggregator.aggregate_data()
        self.assertEqual(result, {'=== 22-03-2018 ===': self.categories})

    def test_aggregate_data_with_two_dates(self):
        result = self.aggregator1.aggregate_data()
        self.assertEqual(result, {'=== 22-03-2018 ===': self.categories, '=== 23-03-2018 ===': self.categories1})



if __name__ == '__main__':
    unittest.main()