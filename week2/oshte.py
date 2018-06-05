
def anagrams():
    first_word = input("Enter first word:\n")
    second_word = input("Enter second word:\n")
    first_word = first_word.lower()
    second_word = second_word.lower()
    first_histo = char_histogram(first_word)
    second_histo = char_histogram(second_word)
    if first_histo == second_histo:
        return "ANAGRAMS"
    else:
        return "NOT ANAGRAMS"


def is_credit_card_valid(number):
    num_digits = to_digits(number)
    if len(num_digits) % 2 == 0:
        return False
    else:
        for x in range(0, len(num_digits)):
            if (len(num_digits) - x - 1) % 2 != 0:
                num_digits[x] = num_digits[x] * 2
                if(num_digits[x] >= 10):
                    num_digits[x] -= 9
        return sum(num_digits) % 10 == 0


def goldbach(n):
    from second import prime
    return list(filter((lambda x: prime(x[0]) and prime(x[1])),[(i, n - i) for i in range(1, n // 2)]))



def drop_bomb(m, row, col, el):
    if row >= 0 and row < len(m) and col >= 0 and col < len(m[row]):
        m[row][col] -= el
        if m[row][col] < 0:
            m[row][col] = 0
        return


def drop_on_all(m, row, col, el):
    drop_bomb(m, row - 1, col - 1, el)
    drop_bomb(m, row - 1, col, el)
    drop_bomb(m, row - 1, col + 1, el)
    drop_bomb(m, row, col - 1, el)
    drop_bomb(m, row, col + 1, el)
    drop_bomb(m, row + 1, col - 1, el)
    drop_bomb(m, row + 1, col, el)
    drop_bomb(m, row + 1, col + 1, el)


def matrix_bombing_plan(m):
    dict = {}
    for row in range(0, len(m)):
        for col in range(0, len(m[row])):
            copie = list(map(list, m))
            save = m[row][col]
            drop_on_all(copie, row, col, save)
            dict[(row, col)] = sum([sum(row) for row in copie])
    return dict


# print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def reduce_file_path(path):
    reduced = '/'
    path_list = path.split('/')
    path_list = list(filter((lambda x: x != ''), path_list))
    #print(path_list)
    result = []
    for i in range(0, len(path_list)):
        if path_list[i] == '.':
            continue
        elif path_list[i] == '..':
            if len(result) > 0:
                result.pop()
        else:
            result += [path_list[i]]
    for i in range(0, len(result)):
        reduced += result[i]
        if i < len(result) - 1:
            reduced += '/'
    return reduced


#print(reduce_file_path("/"))
#print(reduce_file_path("/srv/../"))
#print(reduce_file_path("/srv/www/htdocs/wtf/"))
#print(reduce_file_path("/srv/www/htdocs/wtf"))
#print(reduce_file_path("/srv/./././././"))
#print(reduce_file_path("/etc//wtf/"))
#print(reduce_file_path("/etc/../etc/../etc/../"))
#print(reduce_file_path("//////////////"))
#print(reduce_file_path("/../"))
