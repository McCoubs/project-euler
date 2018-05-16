import math
from helper_functions.get_primes import eratosthenes_primes


def find_nth_prime(nth_prime):
    """
    Function returns the nth prime of the natural numbers.

    :param nth_prime: {int} is nth prime to return in natural numbers
    :return: {int} the nth prime in natural numbers
    """

    # check input, raise relevant errors
    if type(nth_prime) != int:
        raise TypeError("Input param 'nth_prime' was not type of int")
    if nth_prime <= 0:
        raise ValueError("Input param 'nth_prime' was a negative/zero value")

    # by the prime number theorem:
    # n(lnn) + n((ln(lnn))−1) < pn < n(lnn) + n(ln(lnn)), where n=nth, pn=nth prime for n≥6
    if nth_prime >= 6:
        upper_bound = math.ceil(nth_prime * math.log(nth_prime) + nth_prime * math.log(math.log(nth_prime)))
    # else the 5th prime caps at 11
    else:
        upper_bound = 11
    # get all primes up to the calculated possible upper bound of the nth prime
    primes = eratosthenes_primes(upper_bound)

    # return the nth prime from calculated primes
    return primes[nth_prime - 1]

