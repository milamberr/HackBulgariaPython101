class Bill:
    def __init__(self, amount):
        self.amount = amount

    def is_valid(self):
        if type(self.amount) is not int:
            raise TypeError
        elif self.amount < 0:
            raise ValueError

    def __str__(self):
        self.is_valid()
        return str(self.amount)

    def __repr__(self):
        self.is_valid()
        return str(self.amount)

    def __int__(self):
        self.is_valid()
        return int(self.amount)

    def __eq__(self, other):
        self.is_valid()
        return self.amount == other.amount

    def __hash__(self):
        self.is_valid()
        return hash(self.amount)
