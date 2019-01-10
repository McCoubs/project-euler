from project_euler.helper_functions.get_primes import eratosthenes_primes


def summation_of_primes(limit):
    """
    Function will sum all of the primes up to and including the limit given

    Uses the sieve of eratosthenes to generate primes
    :param limit: {int}
    :return: {int} sum of primes up tp limit
    """

    # check input, raise relevant errors
    if type(limit) != int:
        raise TypeError("Input param 'limit' was not type of int")

    # initialize sum and get all primes
    prime_sum = 0
    primes = eratosthenes_primes(limit)

    # add up all primes
    for prime in primes:
        prime_sum = prime_sum + prime

    return prime_sum
