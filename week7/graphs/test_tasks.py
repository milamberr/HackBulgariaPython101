import unittest
from tasks import deep_find, deep_find_all, deep_update, deep_apply, deep_compare,\
                    schema_validator


class TasksTests(unittest.TestCase):
    def test_deep_find(self):
        data = {
            'key1': 'val1',
            'key2': 'val2',
            'key3': {
                'inner_key1': 'val1',
                'inner_key2': 'val2'
            }
        }
        self.assertEqual(deep_find(data, 'key2'), 'val2')
        self.assertEqual(deep_find(data, 'inner_key1'), 'val1')
        self.assertEqual(deep_find(data, 'pesho'), None)

    def test_deep_find_all(self):
        data1 = {
            'key1': 'val1',
            'key2': 'val2',
            'key3': {
                'key1': 'val3',
                'inner_key2': 'val4'
            }
        }
        self.assertEqual(deep_find_all(data1, 'key1'), ['val1', 'val3'])
        self.assertEqual(deep_find_all(data1, 'key2'), ['val2'])
        self.assertEqual(deep_find_all(data1, 'pesho'), [])

    def test_deep_update(self):
        with self.subTest('Data of Key is not dict'):
            data1 = {
                'key1': 'val1',
                'key2': 'val2',
                'key3': {
                    'key1': 'val3',
                    'inner_key2': 'val4'
                }
            }
            expected = {
                'key1': 'pesho',
                'key2': 'val2',
                'key3': {
                    'key1': 'pesho',
                    'inner_key2': 'val4'
                }
            }
            self.assertEqual(deep_update(data1, 'key1', 'pesho'), expected)

        with self.subTest('Data of Key is dict'):
            data1 = {
                'key1': 'val1',
                'key2': 'val2',
                'key3': {
                    'key1': 'val3',
                    'inner_key2': 'val4'
                }
            }

            expected = {
                'key1': 'val1',
                'key2': 'val2',
                'key3': 'pesho'
            }
            self.assertEqual(deep_update(data1, 'key3', 'pesho'), expected)

    def test_deep_apply(self):
        with self.subTest('No sub dictionaries'):
            data1 = {
                'key1': 1,
                'key2': 2,
                'key3': 3
            }
            expected = {
                '1yek': 1,
                '2yek': 2,
                '3yek': 3
            }
            self.assertEqual(deep_apply(expected, lambda x: x[::-1]), data1)

        with self.subTest('Sub dictionary'):
            data1 = {
                'key1': 'val1',
                'key2': 'val2',
                'key3': {
                    'key1': 'val3',
                    'inner_key2': 'val4'
                }
            }
            expected = {
                '1yek': 'val1',
                '2yek': 'val2',
                '3yek': {
                    '1yek': 'val3',
                    '2yek_renni': 'val4'
                }
            }
            self.assertEqual(deep_apply(expected, lambda x: x[::-1]), data1)

    def test_deep_compare(self):
        with self.subTest("No sub dicts"):
            data1 = {
                'key1': 1,
                'key2': 2,
                'key3': 3
            }
            data2 = {
                'key1': 1,
                'key2': 2,
                'key3': 3
            }
            self.assertTrue(deep_compare(data1, data2))
        with self.subTest("Sub dict"):
            expected1 = {
                '1yek': 'val1',
                '2yek': 'val2',
                '3yek': {
                    '1yek': 'val3',
                    '2yek_renni': 'val4'
                }
            }
            expected2 = {
                '1yek': 'val1',
                '2yek': 'val2',
                '3yek': {
                    '1yek': 'val3',
                    '2yek_renni': 'val4'
                }
            }
            self.assertTrue(deep_compare(expected1, expected2))

        with self.subTest("With lists"):
            expected1 = {
                '1yek': 'val1',
                '2yek': ['val2', 'val6', 'val15'],
                '3yek': {
                    '1yek': 'val3',
                    '2yek_renni': 'val4'
                }
            }
            expected2 = {
                '1yek': 'val1',
                '2yek': ['val2', 'val6', 'val15'],
                '3yek': {
                    '1yek': 'val3',
                    '2yek_renni': 'val4'
                }
            }
            self.assertTrue(deep_compare(expected1, expected2))

        with self.subTest("Not equal"):
            expected1 = {
                '1yek': 'val1',
                '2yek': ['val2', 'val6', 'val16'],
                '3yek': {
                    '1yek': 'val3',
                    '2yek_renni': 'val4'
                }
            }
            expected2 = {
                '1yek': 'val1',
                '2yek': ['val2', 'val6', 'val15'],
                '3yek': {
                    '1yek': 'val3',
                    '2yek_renni': 'val4'
                }
            }
            self.assertFalse(deep_compare(expected1, expected2))

    def test_schema_validator(self):
        schema = [
            'key1',
            'key2',
            [
                'key3',
                ['inner_key1', 'inner_key2']
            ]
        ]
        data = {
            'key1': 'val1',
            'key2': 'val2',
            'key3': {
                'inner_key1': 'val1',
                'inner_key2': 'val2'
            }
        }
        invalid_data = {
            'key1': 'val1',
            'key2': 'val2',
            'key3': {
                'inner_key1': 'val1',
                'inner_key2': 'val2'
            },
            'key4': 'not expected'
        }
        self.assertTrue(schema_validator(schema, data))
        self.assertFalse(schema_validator(schema, invalid_data))
if __name__ == '__main__':
    unittest.main()
