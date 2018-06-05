

class Mixin:
    def __init__(self):
        self.x = 0

    def what(self):
        print(globals())


def main():
    print(globals())


if __name__ == '__main__':
    main()
