from category import Category, Expense, Income


class AggregateData:
    def __init__(self, dict_with_dates):
        self.dict_with_dates = dict_with_dates
        self.aggregated_data = {}

    @classmethod
    def aggregate_object(self, data_str):
        attributes = data_str.split(', ')
        if attributes[2] == 'New Income':
            return Income(attributes[0], attributes[1])
        if attributes[2] == 'New Expense':
            return Expense(attributes[0], attributes[1])

    @classmethod
    def aggregate_data_in_a_date(self, data_to_aggregate):
        aggregated_data = []
        for obj in data_to_aggregate:
            aggr_obj = self.aggregate_object(obj)
            aggregated_data.append(aggr_obj)
        return aggregated_data

    def aggregate_data(self):
        for date in self.dict_with_dates.keys():
            self.aggregated_data[date] = self.aggregate_data_in_a_date(self.dict_with_dates[date])
        return self.aggregated_data

    def __repr__(self):
        return str(self.aggregated_data)


