def eratosthenes_primes(upper_bound):
    """
    Function returns a list of all primes up to a given number.

    Uses the Sieve of Eratosthenes method for finding primes.

    :param upper_bound: {int} upper bound
    :return: {list of ints} is list of primes up to maximum
    """

    # initialize arrays for storage
    non_primes = []
    primes = []

    # loop starting at first prime to upper_bound
    for i in range(2, upper_bound + 1):
        # if prime, add to return list
        if i not in non_primes:
            primes.append(i)
            # add all other values to check list
            for j in range(i * i, upper_bound + 1, i):
                non_primes.append(j)

    return primes
