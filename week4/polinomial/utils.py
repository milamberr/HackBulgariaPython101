def is_int(v):
    try:
        int(v)
        return True
    except:
        return False


def extract_variable_and_power(s):
    parts = s.split('^')

    if len(parts) == 1:
        return parts[0], 1

    if len(parts) == 2:
        return parts[0], int(parts[1])

    raise Exception('You should not be here')


def extract_term(s):
    parts = s.split('*')

    if len(parts) == 1:
        if is_int(parts[0]):
            return int(parts[0]), None, None
        else:
            return (1, *extract_variable_and_power(parts[0]))

    if len(parts) == 2:
        return (int(parts[0]), *extract_variable_and_power(parts[1]))

    raise Exception('You should not be here')


def extract_coefficient(s):
    parts = s.split('*')

    if is_int(parts[0]):
        return int(parts[0])

    return 1
