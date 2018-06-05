def sum_of_digits(n):
    return sum(int(i) for i in str(abs(n)))


def to_digits(n):
    return [int(digit) for digit in str(n)]


def to_number(digits):
    return int(''.join(map(str, digits)))


def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


def fact_digits(n):
    return sum([fact(digit) for digit in to_digits(n)])


def fibonacci(n):
    first, second = 0, 1
    numbers = []
    while(n > 0):
        numbers.append(second)
        n -= 1
        first, second = second, first + second

    return numbers


def fib_number(n):
    return ''.join(map(str, fibonacci(n)))


def palindrome(item):
    return str(item) == str(item)[::-1]


def count_vowels(string):
    count = 0
    for x in string.lower():
        if x in 'aeoiuy':
            count += 1
    return count


def count_consonants(string):
    count = 0
    for x in string.lower():
        if x in 'bcdfghjklmnpqrstvxz':
            count += 1
    return count


def char_histogram(string):
    dicti = {}
    for x in string:
        if x in dicti:
            dicti[x] += 1
        else:
            dicti[x] = 1
    return dicti
