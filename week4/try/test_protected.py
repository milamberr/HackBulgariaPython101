class Panda:
    def __init__(self, hrana):
        self.__hrana = hrana

    @property
    def hrana(self):
        return self.__hrana


def main():
    p = Panda(5)
    print(type(type(Panda)))


if __name__ == '__main__':
    main()
