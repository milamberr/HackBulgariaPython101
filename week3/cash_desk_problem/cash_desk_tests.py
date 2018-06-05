import unittest

from bill import Bill
from batch_bill import BatchBill
from cash_desk import CashDesk


class CashDeskTests(unittest.TestCase):
    def setUp(self):
        self.desk = CashDesk()
        self.desk.bills = [Bill(1), Bill(2), Bill(3)]
        self.desk2 = CashDesk()
        self.desk2.bills = [Bill(4), Bill(5), Bill(6)]

    def test_total(self):
        self.assertEqual(self.desk.total(), 6)
        self.assertEqual(self.desk2.total(), 15)

    def test_take_money_from_a_bill(self):
        self.desk.take_money(Bill(5))
        self.assertEqual(self.desk.total(), 11)
        self.desk.take_money(BatchBill([Bill(1), Bill(2), Bill(3)]))
        self.assertEqual(self.desk.total(), 17)


if __name__ == '__main__':
    unittest.main()
