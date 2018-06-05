import json


def read_json(filename):
    if type(filename) is not str or '.json' not in filename:
        raise TypeError
    with open(filename) as f:
        data = json.load(f)
    return data


def best_people(user_data):
    validation(user_data)
    best = {}
    if len(user_data) == 0:
        return {}
    for person in user_data['people']:
        for language in person["skills"]:
            if language["name"] in best:
                if language["level"] > best[language["name"]][2]:
                    best[language["name"]] = [person['first_name'], person['last_name'], language["level"]]
            else:
                best[language['name']] = [person['first_name'], person['last_name'], language["level"]]

    for x in best.keys():
        best[x].pop()
    return best


def validate_main_key_user_data(user_data):
    if type(user_data) is not dict:
        raise TypeError
    if 'people' not in user_data.keys():
        raise TypeError


def validate_values_are_list(people):
    if type(people) is not list:
        raise TypeError


def validate_person_info(person):
    if type(person) is not dict:
        raise TypeError
    for key in ['first_name', 'last_name', 'skills']:
        if key not in person:
            raise TypeError
    if type(person['first_name']) is not str:
        raise TypeError
    if type(person['last_name']) is not str:
        raise TypeError
    if type(person['skills']) is not list:
        raise TypeError


def validate_skills_info(skills):
    if type(skills) is not list:
        raise TypeError
    for skill in skills:
        if type(skill) is not dict:
            raise TypeError
        for x in ['name', 'level']:
            if x not in skill.keys():
                raise TypeError
        if type(skill['name']) is not str:
            raise TypeError
        if type(skill['level']) is not int:
            raise TypeError


def validation(user_data):
    validate_main_key_user_data(user_data)
    validate_values_are_list(user_data['people'])
    for person in user_data['people']:
        validate_person_info(person)
        validate_skills_info(person['skills'])


def main():
    user_data = read_json('data.json')
    print(best_people(user_data))


if __name__ == '__main__':
    main()