import sys
from cat import cat


def cat2(arguments):
    for i in range(1, len(arguments)):
        print(cat(arguments[i]))


def main():
    cat2(sys.argv)


if __name__ == '__main__':
    main()
