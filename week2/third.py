#from first import to_digits
#from first import palindrome
#from second import group
#from first import char_histogram


def to_digits(n):
    return [int(digit) for digit in str(n)]


def palindrome(item):
    return str(item) == str(item)[::-1]


def char_histogram(string):
    dicti = {}
    for x in string:
        if x in dicti:
            dicti[x] += 1
        else:
            dicti[x] = 1
    return dicti


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


def is_number_balanced(number):
    num_list = to_digits(number)

    first_part = [num_list[i] for i in range(0, len(num_list) // 2)]
    if len(num_list) % 2 == 0:
        second_part = [num_list[i] for i in range(len(num_list) // 2, len(num_list))]
    else:
        second_part = [num_list[i] for i in range(len(num_list) // 2 + 1, len(num_list))]
    return sum(first_part) == sum(second_part)


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


def get_largest_palindrome(n):
    for x in reversed(range(0, n)):
        if palindrome(x):
            return x


def sum_of_numbers(input_string):
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


def birthday_ranges(birthdays, ranges):
    result = []
    for i in ranges:
        result.append(len(list(filter((lambda x: x >= i[0] and x <= i[1]), birthdays))))
    return result


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
            curr_group.append(people[i])
            curr_weight += people[i][0]
            curr_num_people += 1
            i += 1
        if curr_weight > max_weight or curr_num_people > max_people:
            i -= 1
            curr_group.pop()
        if len(curr_group) != 0:
            min_trips += len(group([x[1] for x in curr_group])) + 1

    return min_trips
