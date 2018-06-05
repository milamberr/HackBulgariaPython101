import unittest


class Test(unittest.TestCase):
    def test_assert_Raises_test(self):
        with self.assertRaises(ValueError):
            raise ValueError


if __name__ == '__main__':
    unittest.main()
