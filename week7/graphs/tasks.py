from collections import Iterable


def deep_find(data, key):
    if not isinstance(data, Iterable):
        return None

    elif type(data) is dict:
        if key in data.keys():
            return data[key]

        for x in data.keys():
            el = deep_find(data[x], key)
            if el is not None:
                return el

    elif type(data) is not str:
        for x in data:
            el = deep_find(x, key)
            if el is not None:
                return el


def deep_find_all(data, key):
    result = []
    if not isinstance(data, Iterable):
        return result

    elif type(data) is dict:
        if key in data.keys():
            result.append(data[key])

        for k in data.keys():
            el = deep_find(data[k], key)
            if el is not None:
                result.append(el)

    elif type(data) is not str:
        for x in data:
            el = deep_find(x, key)
            if el is not None:
                return el

    return result


def deep_update(data, key, val):
    result = {}

    if type(data) is dict:
        for k in data.keys():
            if k == key:
                result[key] = val
            else:
                result[k] = deep_update(data[k], key, val)

    elif type(data) is list:
        result = []
        for x in data:
            result.append(deep_update(x, key, val))

    else:
        return data

    return result


def deep_apply(func, data):
    result = {}

    if type(data) is dict:
        for k in data.keys():
            if type(k) is not tuple:
                result[func(k)] = deep_apply(func, data[k])
            else:
                result_key = (func(k[0]), func(k[1]))
                result[result_key] = deep_apply(func, data[k])

    elif type(data) is list:
        result = []
        for x in data:
            result.append(deep_apply(func, x))
    else:
        return data

    return result


def deep_compare(obj1, obj2):
    result = True
    if type(obj1) is not type(obj2):
        return False
    elif type(obj1) is dict:
        for k in obj1.keys():
            if k not in obj2.keys():
                return False
            else:
                result = result and deep_compare(obj1[k], obj2[k])

    elif isinstance(obj1, Iterable) and type(obj1) is not str:
        if len(obj1) != len(obj2):
            return False
        for tup in list(zip(obj1, obj2)):
                result = result and deep_compare(tup[0], tup[1])
    else:
        result = result and obj1 == obj2

    return result


def schema_validator(schema, data):
    if len(schema) != len(data.keys()):
        return False
    result = True
    for x in schema:
        if type(x) is not list:
            result = result and x in data.keys()
        else:
            if not x[0] in data.keys():
                return False
            else:
                result = result and schema_validator(x[1], data[x[0]])
    return result
