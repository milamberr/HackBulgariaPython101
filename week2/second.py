def count_substrings(haystack, needle):
    return haystack.count(needle, 0)


def sum_matrix(m):
    return sum(sum(m[row]) for row in range(0, len(m)))


def nan_expand(times):
    if times <= 0:
        return
    if times == 1:
        print('Not a NaN')
        return
    print('Not a ', end = "")
    nan_expand(times - 1)


def prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False

    return True


def prime_factorization(n):
    primes = []
    for x in range(2, n + 1):
        if n % x == 0 and prime(x):
            count = 0
            while(n % x == 0):
                count += 1
                n /= x
            primes.append((x, count))

    return primes


def group(lst):
    current_group = [lst[0]]
    result = []
    for item in lst[1:]:
        if item == current_group[0]:
            current_group.append(item)
        else:
            result.append(current_group)
            current_group = [item]
    result.append(current_group)

    return result


def max_consecutive(items):
    return max(map(len, group(items)))


def palindrome(item):
    return str(item) == str(item)[::-1]


def help_rowwise(search_place, word):
    return search_place.count(word, 0, len(search_place))


def vertical(m, col_inx, word):
    col = ''.join(map(str, [m[row][col_inx] for row in range(0, len(m))]))
    if palindrome(word):
        return help_rowwise(col, word)
    return help_rowwise(col, word) + help_rowwise(col[::-1], word)


def diagonal(m, row_inx, col_inx, word):
    diagonal_word = ''.join(m[row_inx + i][col_inx + i]
    for i in range(0, min(len(m) - row_inx, len(m[0]) - col_inx)))
    counter = help_rowwise(diagonal_word, word)
    diagonal_word = ''.join(m[row_inx + i][col_inx - i]
    for i in range(0, min(len(m) - row_inx, col_inx)))
    counter += help_rowwise(diagonal_word, word)
    return counter


def word_counter(m, word):
    counter = 0
    for row in range(0, len(m)):
        counter += help_rowwise(m[row], word)
        counter += diagonal(m, row, 0, word)
        if not palindrome(m[row]):
            counter += help_rowwise(m[row][::-1], word)
    for col in range(0, len(m[0])):
        counter += diagonal(m, 0, col, word)
        counter += vertical(m, col, word)
    counter -= diagonal(m, 0, 0, word)
    return counter


def gas_stations(distance, tank_size, stations):
    check_points = stations + [distance]
    distance_covered = 0
    shortest = []
    tank = tank_size
    start = 1

    while(start < len(check_points)):
        distance_covered += tank
        tank = 0
        if(distance_covered < check_points[start]):
            shortest.append(check_points[start - 1])
            distance_covered = check_points[start - 1]
            tank = tank_size
        start += 1
    return shortest
