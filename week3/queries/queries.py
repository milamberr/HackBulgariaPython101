import csv

filters = {'__startswith': lambda row_el, start: row_el.startswith(start),
           '__contains': lambda row_el, contain: contain in row_el,
           '__gt': lambda row_el, greater: int(row_el) > int(greater),
           '__lt': lambda row_el, lower: int(row_el) < int(lower)}


def filter(filename, **filter_arguments):
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            data.append(row)

    return filter_data_by_arguments(data, **filter_arguments)


def row_matches_filter_arguments(row, **filter_arguments):
    for x in filter_arguments:
        if x == 'order_by':
            continue
        elif x not in row.keys():
            newkey = x.split('__')[1]
            newkey = '__{}'.format(newkey)
            oldkey = x.split('__')[0]
            if not filters[newkey](row[oldkey], filter_arguments[x]):
                return False
        elif row[x] != filter_arguments[x]:
            return False
    return True


def filter_data_by_arguments(data, **filter_arguments):
    result = []
    for row in data:
        if row_matches_filter_arguments(row, **filter_arguments):
            result.append(row)

    if 'order_by' in filter_arguments.keys():
        sort_key = get_sort_key(result, filter_arguments['order_by'])
        sorted(result, lambda row: row[sort_key][1])

    return result


def get_sort_key(data, sort_key):
    for row in data:
        for i in range(row):
            if row[i][0] == sort_key:
                return i


def order_by(row1_el, row2_el, order):
    return row1_el < row2_el


def count(data, **filter_arguments):
    return len(filter_data_by_arguments(data, **filter_arguments))


def first(data, **filter_arguments):
    result = filter_data_by_arguments(data, **filter_arguments)
    if len(result) > 0:
        return result[0]


def last(data, **filter_arguments):
    result = filter_data_by_arguments(data, **filter_arguments)
    if len(result) > 0:
        return result[len(result) - 1]


def main():
    pass


if __name__ == '__main__':
    main()
