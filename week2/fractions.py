def gcd(num1, num2):
    if type(num1) is not int or type(num2) is not int:
        raise TypeError
    if num2 == 0 or num1 == 0:
        raise ZeroDivisionError
    if num1 == num2:
        return num1
    if num1 > num2:
        return gcd(num1 - num2, num2)
    return gcd(num1, num2 - num1)


def simplify_fraction(fraction):
    numer = fraction[0]
    denom = fraction[1]
    divisor = gcd(abs(numer), abs(denom))
    return (numer // divisor, denom // divisor)


def collect_fractions(fractions):
    if type(fractions) is not list:
        raise TypeError
    summed_nominator, summed_denominator = 0, 1
    for fraction in fractions:
        if type(fraction) is not tuple or type(fraction[0]) is not int or type(fraction[1]) is not int:
            raise TypeError
        elif fraction[1] == 0:
            raise ZeroDivisionError
        else:
            summed_nominator = summed_nominator * fraction[1] + summed_denominator * fraction[0]
            summed_denominator *= fraction[1]
            simplified = simplify_fraction((summed_nominator, summed_denominator))
            summed_nominator, summed_denominator = simplified[0], simplified[1]
    return (summed_nominator, summed_denominator)


def compare_fractions(fr1, fr2):
    if type(fr1[0]) is not int or type(fr1[1]) is not int or type(fr2[0]) is not int or type(fr2[1]) is not int:
        raise TypeError

    return fr1[0] * fr2[1] > fr2[0] * fr1[1]


def sort_fractions(fractions):
    if type(fractions) is not list:
        raise TypeError
    for fraction in fractions:
        if type(fraction) is not tuple:
            raise TypeError
    return sorted(fractions, key=compare_fractions)
