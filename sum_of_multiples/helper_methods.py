def greatest_common_divisor(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a


def least_common_multiple(a, b):
    """Return lowest common multiple, using Euclid's method for gcd"""
    return a * b // greatest_common_divisor(a, b)
