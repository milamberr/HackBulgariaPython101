import unittest
from queries import filter_data_by_arguments

TEST_DATA = [{'full_name': 'Richard Gilbert', 'favourite_color': 'yellow', 'phone_number': '+05(3)2405072219', 'company_name': 'Collins, Bowman and Thompson', 'salary': '3555', 'email': 'elizabethwhite@yahoo.com'},
                {'full_name': 'Emily Brown', 'favourite_color': 'olive', 'phone_number': '(251)374-2829x38582', 'company_name': 'White-Turner', 'salary': '5742', 'email': 'garrisonsusan@yahoo.com'},
                {'full_name': 'Margaret David', 'favourite_color': 'fuchsia', 'phone_number': '1-962-531-9170', 'company_name': 'Larson LLC', 'salary': '1699', 'email': 'christensencarol@gmail.com'},
                {'full_name': 'Helen Williams', 'favourite_color': 'green', 'phone_number': '(309)636-9346', 'company_name': 'Zamora-Pierce', 'salary': '8104', 'email': 'lhale@hotmail.com'},
                {'full_name': 'Tonya Clark', 'favourite_color': 'gray', 'phone_number': '1-441-553-2992', 'company_name': 'Gilmore-Wang', 'salary': '409', 'email': 'heather39@yahoo.com'},
                {'full_name': 'Maria Powers', 'favourite_color': 'green', 'phone_number': '937.363.3968x63560', 'company_name': 'Gutierrez, Webb and Cox', 'salary': '7267', 'email': 'salazartiffany@hotmail.com'}]


GREEN_FILTERED_DATA = [TEST_DATA[3], TEST_DATA[5]]

GREEN_SALARY_FILTERED_DATA = [TEST_DATA[5]]


class FilterQueriesTests(unittest.TestCase):
    def test_filter_by_one_argument(self):
        self.assertEqual(filter_data_by_arguments(TEST_DATA, favourite_color='green'), GREEN_FILTERED_DATA)

    def test_filter_by_two_arguments(self):
        self.assertEqual(filter_data_by_arguments(TEST_DATA, favourite_color='green', salary='7267'), GREEN_SALARY_FILTERED_DATA)

    def test_filter_starts_with(self):
        self.assertEqual(filter_data_by_arguments(TEST_DATA, full_name__startswith='Maria'), GREEN_SALARY_FILTERED_DATA)

    def test_filter_contains(self):
        self.assertEqual(filter_data_by_arguments(TEST_DATA, company_name__contains='Gilmore'), [TEST_DATA[4]])

    def test_filter_lower_than(self):
        self.assertEqual(filter_data_by_arguments(TEST_DATA, salary__lt='2000'), [TEST_DATA[2], TEST_DATA[4]])


if __name__ == '__main__':
    unittest.main()
