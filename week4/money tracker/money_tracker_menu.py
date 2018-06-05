import sys
import re
from money_tracker import MoneyTracker
from exceptions import NegativeAmountError


class MoneyTrackerMenu:
    def __init__(self, money_tracker):
        self.tracker = money_tracker

    def valid_input_income_expense_attributes(self, income_category, money, date):
        try:
            money = int(money)
        except ValueError:
                money = float(money)

        if re.match('\d\d-\d\d-\d\d\d\d', date) is None:
            raise TypeError
        if money < 0:
            raise NegativeAmountError

    def show_data_for_specific_date(self):
            print("Enter date:")
            while(True):
                date = input()
                if re.match('\d\d-\d\d-\d\d\d\d', date) is not None:
                    self.tracker.show_user_data_per_date(date)
                    break
                else:
                    print("Invalid input format!Please try again:")

    def add_income(self):
        print("Enter income_category, money and date")
        while(True):
            income_category = input()
            money = input()
            date = input()
            try:
                self.valid_input_income_expense_attributes(income_category, money, date)
                self.tracker.add_income(income_category, money, date)
                print("Income added successfully!")
                break
            except TypeError:
                print("Invalid input format!Please try again.")

            except NegativeAmountError:
                print("Invalid amount of money!Please try again.")

    def add_expense(self):
        print("Enter expense_category, money and date")
        while(True):
            expense_category = input()
            money = input()
            date = input()
            try:
                self.valid_input_income_expense_attributes(expense_category, money, date)
                self.tracker.add_expense(expense_category, money, date)
                print("Expense added successfully!")
                break
            except TypeError:
                print("Invalid input format!Please try again.")
            except NegativeAmountError:
                print("Invalid amount of money!Please try again.")

    def start_menu(self):
        opt = -1
        show_message = """Choose one of the following options to continue:
        1 - show all data
        2 - show data for specific date
        3 - show expenses, ordered by categories
        4 - add new income
        5 - add new expense
        6 - exit"""
        while(True):
            print(show_message)
            opt = input()
            try:
                opt = int(opt)
                if opt == 1:
                    print(self.tracker.list_user_data())
                elif opt == 2:
                    self.show_data_for_specific_date()
                elif opt == 3:
                    print(self.tracker.list_user_expenses_ordered_by_categories())
                elif opt == 4:
                    self.add_income()
                elif opt == 5:
                    self.add_expense()
                elif opt == 6:
                    sys.exit()
                elif opt < 0 or opt > 6:
                    print("Please enter a valid option")
            except ValueError:
                print("You have not entered a number!Please try again.")
