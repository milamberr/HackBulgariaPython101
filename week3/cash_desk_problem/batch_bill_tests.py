import unittest
from bill import Bill
from batch_bill import BatchBill


class BatchBillTests(unittest.TestCase):
    def setUp(self):
        bills = []
        bills.append(Bill(5))
        bills.append(Bill(15))
        bills.append(Bill(11))
        bills.append(Bill(7))
        bills.append(Bill(2))
        self.batch_bill = BatchBill(bills)
        self.empty_batch_bill = BatchBill([])

    def test_len(self):
        self.assertEqual(self.batch_bill.__len__(), 5)

    def test_len_with_empty(self):
        self.assertEqual(self.empty_batch_bill.__len__(), 0)

    def test_sum(self):
        self.assertEqual(self.batch_bill.total(), 40)

    def test_sum_with_empty(self):
        self.assertEqual(self.empty_batch_bill.total(), 0)

    def test_iterate_over_bills(self):
        sum_bills = 0
        for bill in self.batch_bill:
            sum_bills += int(bill)

        self.assertEqual(self.batch_bill.total(), sum_bills)


if __name__ == '__main__':
    unittest.main()
