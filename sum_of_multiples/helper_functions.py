def greatest_common_divisor(a, b):
    """
    Function returns greatest common divisor using Euclid's Algorithm.

    REQ: a, b >= 0 and whole

    :param a: {int}
    :param b: {int}
    :return: {int} greatest common divisor of a and b
    """
    while b:
        a, b = b, a % b
    return a


def least_common_multiple(a, b):
    """
    Function returns lowest common multiple, using Euclid's method for gcd.

    REQ: a, b >= 0 and whole

    :param a: {int}
    :param b: {int}
    :return: {int} least common multiple of a and b
    """
    return a * b // greatest_common_divisor(a, b)
