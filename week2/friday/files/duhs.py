import sys
import os
from os.path import getsize
from os.path import isfile, join


def duhs(filepath):
    try:
        return getsize(filepath)
    except FileNotFoundError as error:
        print(error)


def size_of_dir(dirpath):
    totalsize = 0
    dir_content = os.listdir(dirpath)
    while len(dir_content) > 0:
        curr_el = dir_content[len(dir_content) - 1]
        dir_content.pop()
        if isfile(join(dirpath, curr_el)):
            totalsize += duhs(curr_el)
        else:
            dir_content += os.listdir(curr_el)

    return totalsize


def main():
    print(size_of_dir(sys.argv[1]))


if __name__ == '__main__':
    main()
