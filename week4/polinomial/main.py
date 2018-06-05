from term import Polynomial


def main():
    function = input("Enter function:")
    polinom = Polynomial.parse_from_string(function)
    polinom = polinom.derivative()
    print(f'Derivative of f(x) = {function} is:\n{str(polinom)}')


if __name__ == '__main__':
    main()
