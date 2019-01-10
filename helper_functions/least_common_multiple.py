from project_euler.helper_functions.greatest_common_divisor import greatest_common_divisor


def least_common_multiple(a, b):
    """
    Function returns lowest common multiple, using Euclid's method for gcd.

    REQ: a, b >= 0 and whole

    :param a: {int}
    :param b: {int}
    :return: {int} least common multiple of a and b
    """
    return a * b // greatest_common_divisor(a, b)
