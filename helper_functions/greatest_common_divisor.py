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
