import sys


def sum_numbers(filename):
    with open(filename) as f:
        numbers_str = f.read()
        print(numbers_str)
        return sum(list(map(int, numbers_str[:-1].split(' '))))


def main():
    print(sum_numbers(sys.argv[1]))


if __name__ == '__main__':
    main()
