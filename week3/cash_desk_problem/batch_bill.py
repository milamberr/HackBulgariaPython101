from copy import deepcopy


class BatchBill:
    def __init__(self, bills):
        self.bills = deepcopy(bills)

    def __len__(self):
        return len(self.bills)

    def total(self):
        return sum([int(x) for x in self.bills])

    def __getitem__(self, index):
        return self.bills[index]


