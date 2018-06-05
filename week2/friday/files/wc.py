import sys
import os
from os.path import getsize


def count(arguments):
    with open(arguments[2]) as f:
        content = f.read()
        if arguments[1] == 'chars':
            return len(content)
        elif arguments[1] == 'words':
            return len(content.split(' '))
        elif arguments[1] == 'lines':
            return len(content.split('\n'))


def main():
    print(count(sys.argv))


if __name__ == '__main__':
    main()