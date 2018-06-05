from random import randint


def gen_newline():
    if randint(1, 5) == 5:
        return '\n'
    return ''


class BookGenerator:
    def __init__(self, count, chapter_length):
        self.count = count
        self.chapter_length = chapter_length
        self.curr_chapter = 1

    def generate_new_chapter(self):
        word_generator = self.generate_new_word()
        while(True):
            curr_length = self.chapter_length
            chapter = f'# Chapter {self.curr_chapter}\n'

            for word in word_generator:
                chapter = f'{chapter} {word}{gen_newline()}'
                curr_length -= 1
                if curr_length <= 0:
                    break
            
            self.curr_chapter += 1
            yield chapter

    def generate_new_word(self):
        while(True):
            word_len = randint(1, 15)
            word = ''
            for i in range(word_len):
                word = f'{word}{chr(randint(97,122))}'

            yield word

    def gen_book(self):
        with open('book.txt', 'w') as book:
            chapter_generator = self.generate_new_chapter()

            for chapter in chapter_generator:
                book.write(f'{chapter}\n\n')
                if self.curr_chapter == self.count:
                    break


def main():
    a = BookGenerator(4000, 10000)
    a.gen_book()


if __name__ == '__main__':
    main()

