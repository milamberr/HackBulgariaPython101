from test import Mixin


class Inh(Mixin):
    def __init__(self):
        pass


def main():
    print(globals())
    #p = Inh()
    #p.what()


if __name__ == '__main__':
    main()
