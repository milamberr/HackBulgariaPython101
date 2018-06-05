from coding_skills import read_json
from coding_skills import best_people
from coding_skills import validation,
                            validate_person_info,
                            validate_skills_info,
                            validate_main_key_user_data,
                            validate_values_are_list
import unittest

LIST_FOR_ONE_PERSON_TEST = {
    "people": [{
                    "first_name": "Ivo",
                    "last_name": "Ivo",
                    "skills": [{
                        "name": "C++",
                        "level": 30
                    }, {
                        "name": "PHP",
                        "level": 25
                    }, {
                        "name": "Python",
                        "level": 80
                    }, {
                        "name": "C#",
                        "level": 25
                    }]
                }]
}

LIST_FOR_ONE_LANGUAGE = {
    "people": [{
                "first_name": "Pesho",
                "last_name": "Petrov",
                "skills": [{

                    "name": "Javascript",
                    "level": 40
                          }]
                }]
}

LIST_FOR_TWO_PEOPLE_TEST = {
    "people": [{
                    "first_name": "Pesho",
                    "last_name": "Pesho",
                    "skills": [{
                        "name": "C++",
                        "level": 150
                    }, {
                        "name": "Java",
                        "level": 21
                    }]
    },{
                    "first_name": "Ninjata",
                    "last_name": "bahti_ludiq",
                    "skills": [{
                        "name": "C++",
                        "level": 23
                    }, {
                        "name": "Java",
                        "level": 9000
                    }]
    }]
}

class CodingSkills_Tests(unittest.TestCase):
    def test_open_json_file(self):
        with self.assertRaises(FileNotFoundError):
            read_json('not_existing.json')

    #def test_file_is_empty(self):
    #    self.assertEqual(read_json('empty.json'), {})

    def test_correct_filename(self):
        with self.assertRaises(TypeError):
            read_json('some.txt')
        with self.assertRaises(TypeError):
            read_json(123)

    def test_empty_data_result(self):
        self.assertEqual(best_people({}), {})

    def test_one_person_data(self):
        self.assertEqual(best_people(LIST_FOR_ONE_PERSON_TEST),
                  {'C++': ['Ivo','Ivo'],
                   'PHP': ['Ivo', 'Ivo'],
                   'Python': ['Ivo', 'Ivo'],
                   'C#': ['Ivo', 'Ivo']})

    def test_one_language(self):
        self.assertEqual(best_people(LIST_FOR_ONE_LANGUAGE), {'Javascript': ['Pesho', 'Petrov']})

    def test_two_people_two_languages(self):
        self.assertEqual(best_people(LIST_FOR_TWO_PEOPLE_TEST), {'Java': ['Ninjata', 'bahti_ludiq'], 'C++': ['Pesho', 'Pesho']})

    def test_valid_type_user_data(self):
        with self.assertRaises(TypeError):
            validate_main_key_user_data('not_dic')
        with self.assertRaises(TypeError):
            validate_main_key_user_data({'not_people': 1})

    def test_valid_type_user_data_values(self):
        with self.assertRaises(TypeError):
            validate_values_are_list('not_list')

    def test_valid_person_info(self):
        with self.assertRaises(TypeError):
            validate_person_info('not dic')
        with self.assertRaises(TypeError):
            validate_person_info({'not_first_name': 'pesho', 'last_name': 'pesho', 'skills': []})
        with self.assertRaises(TypeError):
            validate_person_info({'first_name': 'pesho', 'not_last_name': 'pesho', 'skills': []})
        with self.assertRaises(TypeError):
            validate_person_info({'first_name': 'pesho', 'last_name': 'pesho', 'not_skills': []})
        with self.assertRaises(TypeError):
            validate_person_info({'first_name': 1, 'last_name': 'pesho', 'skills': []})
        with self.assertRaises(TypeError):
            validate_person_info({'first_name': 'pesho', 'last_name': '1', 'skills': []})
        with self.assertRaises(TypeError):
            validate_person_info({'first_name': 'pesho', 'last_name': 'pesho', 'skills': 1})

    def test_valid_skills_info(self):
        with self.assertRaises(TypeError):
            validate_skills_info('not a list')
        with self.assertRaises(TypeError):
            validate_skills_info([{}, 'not a dict'])
        with self.assertRaises(TypeError):
            validate_skills_info([{'not_name': '', 'level': 1}])
        with self.assertRaises(TypeError):
            validate_skills_info([{'name': '', 'not_level': 2}])
        with self.assertRaises(TypeError):
            validate_skills_info([{'name': 1, 'level': 2}])
        with self.assertRaises(TypeError):
            validate_skills_info([{'name': '', 'level': 'not_number'}])


if __name__ == '__main__':
    unittest.main()
