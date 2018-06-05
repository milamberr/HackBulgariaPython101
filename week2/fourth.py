#from first import to_digits
#from first import palindrome
#from second import group
#from first import char_histogram


def is_number_balanced(number):
    num_list = to_digits(number)

    first_part = [num_list[i] for i in range(0, len(num_list) // 2)]
    second_part = [num_list[i] 
        for i in range(len(num_list) // 2 + 1, len(num_list))]
    return sum(first_part) == sum(second_part)


#print(is_number_balanced(1238033))
#print(is_number_balanced(9))
#print(is_number_balanced(4518))
#print(is_number_balanced(28471))
#print(is_number_balanced(1238033))

#use all
def increasing_or_decreasing(seq):
    up = all(seq[i] < seq[i + 1] for i in range(0, len(seq) - 1))
    down = all(seq[i] > seq[i + 1] for i in range(0, len(seq) - 1))
    if up:
        return "Up!"
    elif down:
        return 'Down!'
    else:
        return False


#print(increasing_or_decreasing([1,2,3,4,5]))
# print(increasing_or_decreasing([5,6,-10]))
# print(increasing_or_decreasing([1,1,1,1]))
# print(increasing_or_decreasing([9,8,7,6]))


def get_largest_palindrome(n):
    for x in reversed(range(0, n)):
        if palindrome(x):
            return x


# print(get_largest_palindrome(99))
# print(get_largest_palindrome(252))
# print(get_largest_palindrome(994687))
# print(get_largest_palindrome(754649))


def sum_of_numbers(input_string):
    #pattern = re.compile("[0-9]+")
    #filter
    counter = 0
    sum = 0
    for x in input_string:
        if x >= '0' and x <= '9':
            counter *= 10
            counter += int(x)
        else:
            sum += counter
            counter = 0
    sum += counter
    return sum


# print(sum_of_numbers("ab125cd3"))
# print(sum_of_numbers("ab12"))
# print(sum_of_numbers("ab"))
# print(sum_of_numbers("1101"))
# print(sum_of_numbers("1111O"))
# print(sum_of_numbers("1abc33xyz22"))
# print(sum_of_numbers("0hfabnek"))


def birthday_ranges(birthdays, ranges):
    result = []
    for i in ranges:
        result.append(len(list(filter((lambda x: x >= i[0] and x <= i[1]), birthdays))))
    return result


# print(birthday_ranges([1, 2, 3, 4, 5],
#     [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))
# print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15],
#     [(4, 9), (6, 7), (200, 225), (300, 365)]))


#use dictionary
def numbers_to_message(pressed_sequence):
    letters1 = 'abcdefghijklmno'
    letters2 = 'pqrs'
    letters3 = 'tuv'
    letters4 = 'wxyz'
    message = ''
    cap = False
    groups = group(pressed_sequence)
    for x in groups:
        letter = ''
        if x[0] == 0:
            message += ' '
        elif x[0] == 1:
            cap = True
        else:
            if x[0] != -1 and x[0] < 7:
                letter_inx = (x[0] - 2) * 3 + (len(x) - 1) % 3
                letter = letters1[letter_inx]
            elif x[0] == 7:
                letter = letters2[(len(x) - 1) % 4]
            elif x[0] == 8:
                letter = letters3[(len(x) - 1) % 3]
            elif x[0] == 9:
                letter = letters4[(len(x) - 1) % 3]
            if cap:
                letter = letter.upper()
            message += letter
            cap = False
    return message


#print(numbers_to_message([7, 7, 7, 8, 8, 2, 2, 9, 9, 9]))
#print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))
#print(numbers_to_message([2, 2, 2, 2]))
#print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))


def message_to_numbers(message):
    letters = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    result = []
    for i in range(0, len(message)):
        letter = message[i]
        if letter == ' ':
            result += [0]
        elif letter.isupper():
            result += [1]
            letter = letter.lower()

        for group_letters in range(0, len(letters)):
            if letter in letters[group_letters]:
                for inx in range(0, len(letters[group_letters])):
                    result += [(group_letters + 2)]
                    if letter == letters[group_letters][inx]:
                        break

        for x in letters:
            if i < len(message) - 1:
                if (message[i] in x) and (message[i + 1] in x):
                    result += [-1]

    return result


# print(message_to_numbers("abc"))
# print(message_to_numbers("a"))
# print(message_to_numbers("Ivo e Panda"))
# print(message_to_numbers("aabbcc"))


def elevator_trips(people_weight, people_floors, elevator_floors, max_people, max_weight):
    min_trips = 0
    if len(people_weight) == 0 or len(people_floors) == 0:
        return 0
    people = [(people_weight[i], people_floors[i]) for i in range(0, len(people_floors))]
    i = 0
    curr_weight = 0
    curr_num_people = 0
    while(i < len(people_floors)):
        curr_group = []
        curr_weight = 0
        curr_num_people = 0
        while(i < len(people_floors) and curr_weight <= max_weight and curr_num_people <= max_people):
            curr_group .append(people[i])
            curr_weight += people[i][0]
            curr_num_people += 1
            i += 1
        if curr_weight > max_weight or curr_num_people > max_people:
            i -= 1
            curr_group.pop()
        if len(curr_group) != 0:
            min_trips += len(group(curr_group)) + 1

    min_trips -= 1
    return min_trips


# print(elevator_trips([], [], 5, 2, 200))
# print(elevator_trips([40, 50], [], 5, 2, 200))
# print(elevator_trips([40, 40, 100, 80, 60], [2, 3, 3, 2, 3], 3, 5, 200))
# print(elevator_trips([80, 60, 40], [2, 3, 5], 5, 2, 200))


# extra tasks


def char_histogram(string):
    dicti = {}
    for x in string:
        if x in dicti:
            dicti[x] += 1
        else:
            dicti[x] = 1
    return dicti


def anagrams(first_word, second_word):
    first_word = first_word.lower()
    second_word = second_word.lower()
    first_histo = char_histogram(first_word)
    second_histo = char_histogram(second_word)
    if first_histo == second_histo:
        return "ANAGRAMS"
    else:
        return "NOT ANAGRAMS"


# print(anagrams())

def to_digits(number):
    return [int(digit) for digit in str(number)]


def is_credit_card_valid(number):
    num_digits = to_digits(number)
    if len(num_digits) % 2 == 0:
        return 'Invalid!'
    else:
        for x in range(0, len(num_digits)):
            if (len(num_digits) - x - 1) % 2 != 0:
                num_digits[x] = num_digits[x] * 2
                if(num_digits[x] >= 10):
                    num_digits[x] -= 9
        if sum(num_digits) % 10 == 0:
            return 'Valid!'
        else:
            return 'Invalid!'


# print(is_credit_card_valid(79927398713))
# print(is_credit_card_valid(79927398715))


def goldbach(n):
    from second import prime
    return list(filter((lambda x: prime(x[0]) and prime(x[1])),[(i, n - i) for i in range(1, n // 2)]))


# print(goldbach(100))


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


# print(reduce_file_path("/"))
# print(reduce_file_path("/srv/../"))
# print(reduce_file_path("/srv/www/htdocs/wtf/"))
# print(reduce_file_path("/srv/www/htdocs/wtf"))
# print(reduce_file_path("/srv/./././././"))
# print(reduce_file_path("/etc//wtf/"))
# print(reduce_file_path("/etc/../etc/../etc/../"))
# print(reduce_file_path("//////////////"))
# print(reduce_file_path("/../"))
