from money_tracker import MoneyTracker
from money_tracker_menu import MoneyTrackerMenu
from aggregated_money_tracker import AggregateData
from parse_money_tracker_data import MoneyDataParser


def main():
    while(True):
        file_name = input()
        try:
            parser = MoneyDataParser(file_name)
            data = parser.parse_data()
            print(data)
            aggregator = AggregateData(data)
            tracker = MoneyTracker(aggregator)
            menu = MoneyTrackerMenu(tracker)
            menu.start_menu()
            break
        except FileNotFoundError:
            print("This file doesnt exist!Please try again.")
if __name__ == '__main__':
    main()