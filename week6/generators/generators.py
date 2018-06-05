def chain(iter1, iter2):
    for x in iter1:
        yield x

    for x in iter2:
        yield x


def compress(iterable, mask):
    for i in range(0, len(iterable)):
        if mask[i]:
            yield iterable[i]
        else:
            continue


def cycle(iterable):
    while True:
        for x in iterable:
            yield x


def book_reader(files):
    begin = True
    chapter = ''
    for file in files:
        with open(file) as curr_file:
            curr_line = ''
            while(True):
                curr_line = curr_file.readline()
                if curr_line == '':
                    break
                if begin:
                    chapter += curr_line
                    begin = False
                elif curr_line.startswith('#'):
                    yield chapter
                    chapter = curr_line
                else:
                    chapter += curr_line

    yield chapter


def main():
    from os import listdir
    from os.path import isfile, join
    path = "/home/ivan/HackPython/week6/generators/book"

    onlyfiles = [join(path, f) for f in listdir(path) if isfile(join(path, f))]

    generator_chapters = book_reader(onlyfiles)

    for chapter in generator_chapters:
        input()
        print(chapter)


if __name__ == '__main__':
    main()
            