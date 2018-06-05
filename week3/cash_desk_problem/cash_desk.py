from bill import Bill
from batch_bill import BatchBill


class CashDesk:
    def __init__(self):
        self.bills = []

    def take_money(self, money):
        if type(money) is Bill:
            self.bills.append(money)
        elif type(money) is BatchBill:
            self.bills += [x for x in money]

    def total(self):
        return sum(int(x) for x in self.bills)

    def inspect(self):
        count = 0
        if len(self.bills) == 0:
            return
        last_seen = self.bills[0]
        sorted_bills = self.bills.sorted()
        for x in sorted_bills:
            if last_seen == x:
                count += 1
            else:
                print('{} - {}'.format(last_seen, count))
                count = 0
                last_seen = x
