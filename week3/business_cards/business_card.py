import json
import os
import sys


def generate_head(name):
    return """<head>
                <title>{0} {1}</title>
                <link rel="stylesheet" type="text/css" href="styles.css">
            </head>
    """.format(name[0], name[1])


def generate_outer_div(info):
    basic_info = [info['age'], info['birth_date'], info['birth_place'], info['gender']]
    full_name = [info['first_name'], info['last_name']]
    avatar = info['avatar']
    gender = info['gender']
    interests = info['interests']
    skills = info['skills']
    return """<div class="business-card {0}">
                {1}
                {2}
                {3}
                {4}
                {5}
              </div>""".format(gender,
                               generate_h1(full_name),
                               generate_img(avatar),
                               generate_div_basic_info(basic_info),
                               generate_div_interests(interests),
                               generate_div_skills(skills))


def generate_h1(full_name):
    return '<h1 class="full-name">{0} {1}</h1>'.format(*full_name)


def generate_img(avatar):
    return '<img class="avatar" src="avatars/{0}">'.format(avatar)


def generate_div_basic_info(info):
    return """<div class="base-info">
                  <p>Age: {0}</p>
                  <p>Birth date: {1}</p>
                  <p>Birth place: {2}</p>
                  <p>Gender: {3}</p>
              </div>""".format(*info)


def generate_list_interests(interests):
    ul_str = ''
    for x in interests:
        ul_str = '{0}<li>{1}</li>\n'.format(ul_str, x)
    return ul_str


def generate_div_interests(interests):
    return """ <div class="interests">
                  <h2>Interests:</h2>
                  <ul>
                      {0}
                  </ul>
              </div>""".format(generate_list_interests(interests))


def generate_list_skills(skills):
    ul_str = ''
    for x in skills:
        ul_str = '{0}<li>{1} - {2}</li>\n'.format(ul_str, x['name'], x['level'])
    return ul_str


def generate_div_skills(skills):
    # lambda_print = lambda x: '{} - {}'.format(x['name'], x['level'])
    return """<div class="skills">
                <h2>Skills:</h2>
                <ul>
                    {0}
                </ul>
              </div>""".format(generate_list_skills(skills))


def create_business_card_for_single(person):
    full_name = [person['first_name'], person['last_name']]
    return """
              <!DOCTYPE html>
              <html>
                  {0}
              <body>
                  {1}
              </body>
              </html>""".format(generate_head(full_name), generate_outer_div(person))


def main(filename):
    with open(filename) as f:
        data = json.load(f)

    business_card_names = []
    for person in data['people']:
        rel_path = '{0}_{1}.html'.format(person['first_name'], person['last_name'])
        with open(rel_path, 'w') as f:
            f.write(create_business_card_for_single(person))

        business_card_names.append(f'{person["first_name"]}_{person["last_name"]}.html')

    return business_card_names


if __name__ == '__main__':
    filename = sys.argv[2]
    main(filename)

