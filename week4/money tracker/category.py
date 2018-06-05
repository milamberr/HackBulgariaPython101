class Category:
    def __init__(self, amount, category):
        self._amount = amount
        self._category = category

    def __str__(self):
        return '{"Amount": {1}, "Category": {2}}'.format(self._amount, self._category)

    def __repr__(self):
        return f'Amount:{self._amount},Category:{self._category}'

    def __eq__(self, other):
        return self._amount == other._amount and self._category == other._category


class Income(Category):
    def __init__(self, amount, source):
        super().__init__(amount, source)

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return f'--Income,{super().__repr__()}--'

    def __eq__(self, other):
        return super().__eq__(other)

    @property
    def get_category(self):
        return self._category


class Expense(Category):
    def __init__(self, amount, expense):
        super().__init__(amount, expense)

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return f'--Expense,{super().__repr__()}--'

    def __eq__(self, other):
        return super().__eq__(other)

    @property
    def get_category(self):
        return self._category
