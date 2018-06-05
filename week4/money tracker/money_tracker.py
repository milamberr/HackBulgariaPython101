from aggregated_money_tracker import AggregateData
from category import Expense, Category, Income
from copy import deepcopy


class MoneyTracker:
    def __init__(self, aggregated_money_tracker):
        self.aggregated_money_tracker = aggregated_money_tracker
        self.data = self.aggregated_money_tracker.aggregate_data()

    def list_user_data(self):
        return self.data

    def show_user_savings(self):
        result = []
        for date in self.data.keys():
            for cat in self.data[date]:
                if cat.category() == 'Savings':
                    result.append(cat)
        print(result)

    def show_user_deposits(self):
        result = []
        for date in self.data.keys():
            for cat in self.data[date]:
                if cat.category() == 'Deposits':
                    result.append(cat)
        print(result)

    def show_user_expenses(self):
        result = []
        for date in self.data.keys():
            for cat in self.data[date]:
                if type(cat) is Expense:
                    result.append(cat)
        print(result)

    def list_user_expenses_ordered_by_categories(self):
        result = []
        for date in self.data.keys():
            for cat in self.data[date]:
                if type(cat) is Expense:
                    result.append(cat)
        result.sort(key=lambda cat: cat._category)
        return result

    def show_user_data_per_date(self, date):
        date = self.convert_date(date)
        if date not in self.data.keys():
            print()
        else:
            print(self.data[date])

    def list_income_categories(self):
        result = []
        for date in self.data.keys():
            for cat in self.data[date]:
                if type(cat) is Income:
                    result.append(cat)
        return result

    def list_expense_categories(self):
        result = []
        for date in self.data.keys():
            for cat in self.data[date]:
                if type(cat) is Expense:
                    result.append(cat)
        return result

    def add_income(self, income_category, money, date):
        new_income = Income(money, income_category)
        conv_date = self.convert_date(date)
        if conv_date in self.data.keys():
            self.data[conv_date].append(new_income)
        else:
            self.data[conv_date] = [new_income]

    def add_expense(self, expense_category, money, date):
        new_expense = Expense(money, expense_category)
        conv_date = self.convert_date(date)
        if conv_date in self.data.keys():
            self.data[conv_date].append(new_expense)
        else:
            self.data[conv_date] = [new_expense]

    def convert_date(self, date):
        return '=== {0} ==='.format(date)



