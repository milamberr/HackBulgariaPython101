from third import is_number_balanced, increasing_or_decreasing, get_largest_palindrome, sum_of_numbers, birthday_ranges
from third import numbers_to_message, message_to_numbers, elevator_trips
import unittest


class ThirdTests(unittest.TestCase):
    def test_number_balanced(self):
        self.assertEqual(is_number_balanced(9), True)
        self.assertEqual(is_number_balanced(4518), True)
        self.assertEqual(is_number_balanced(28471), False)
        self.assertEqual(is_number_balanced(1238033), True)

    def test_increasing_or_decreasing(self):
        self.assertEqual(increasing_or_decreasing([1, 2, 3, 4, 5]), 'Up!')
        self.assertEqual(increasing_or_decreasing([5, 6, -10]), False)
        self.assertEqual(increasing_or_decreasing([1, 1, 1, 1]), False)
        self.assertEqual(increasing_or_decreasing([9, 8, 7, 6]), 'Down!')

    def test_largest_palindrome(self):
        self.assertEqual(get_largest_palindrome(99), 88)
        self.assertEqual(get_largest_palindrome(252), 242)
        self.assertEqual(get_largest_palindrome(994687), 994499)
        self.assertEqual(get_largest_palindrome(754649), 754457)

    def test_sum_of_numbers(self):
        self.assertEqual(sum_of_numbers("ab125cd3"), 128)
        self.assertEqual(sum_of_numbers("ab12"), 12)
        self.assertEqual(sum_of_numbers("ab"), 0)
        self.assertEqual(sum_of_numbers("1101"), 1101)
        self.assertEqual(sum_of_numbers("1111O"), 1111)
        self.assertEqual(sum_of_numbers("1abc33xyz22"), 56)
        self.assertEqual(sum_of_numbers("0hfabnek"), 0)

    def test_birthday_ranges(self):
        self.assertEqual(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]), [2, 3, 4, 5, 2])
        self.assertEqual(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15],
                                         [(4, 9), (6, 7), (200, 225), (300, 365)]), [5, 2, 0, 1])

    def test_sms(self):
        self.assertEqual(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]), "abc")
        self.assertEqual(numbers_to_message([2, 2, 2, 2]), "a")
        self.assertEqual(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3,
                                             3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]), "Ivo e Panda")

    def test_message_to_numbers(self):
        self.assertEqual(message_to_numbers("abc"), [2, -1, 2, 2, -1, 2, 2, 2])
        self.assertEqual(message_to_numbers("a"), [2])
        self.assertEqual(message_to_numbers("Ivo e Panda"), [1, 4, 4, 4, 8, 8, 8, 6, 6, 6,
                                                             0, 3, 3, 0, 1, 7, 2, 6, 6, 3, 2])
        self.assertEqual(message_to_numbers("aabbcc"), [2, -1, 2, -1, 2, 2, -1, 2,
                                                        2, -1, 2, 2, 2, -1, 2, 2, 2])

    def test_elevator_trips(self):
        self.assertEqual(elevator_trips([], [], 5, 2, 200), 0)
        self.assertEqual(elevator_trips([40, 50], [], 5, 2, 200), 0)
        self.assertEqual(elevator_trips([40, 40, 100, 80, 60], [2, 3, 3, 2, 3], 3, 5, 200), 6)
        self.assertEqual(elevator_trips([80, 60, 40], [2, 3, 5], 5, 2, 200), 5)




if __name__ == '__main__':
    unittest.main()