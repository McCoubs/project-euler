def sum_of_fibonacci(maximum, sum_even):
    """
    Function returns the sum of all even or odd terms in the fibonacci sequence up to maximum.

    REQ: maximum >= 0 and whole

    :param maximum: {int} is maximum to sum to
    :param sum_even: {bool} determines whether to sum even or odd terms
    :return: {int} sum of even or odd terms in fibonacci sequence up to maximum
    """

    # set first 2 terms of fib
    prev, current = 0, 1
    fib_sum = 0

    # loop until we hit maximum
    while fib_sum <= maximum:

        # set vars, set nprev and current
        prev, current = current, prev + current

        # check if user wants to sum on even and num is even
        if sum_even and current % 2 == 0:
            fib_sum += current
        # check if user wants odd and is odd
        if (not sum_even) and (current % 2 != 0):
            fib_sum += current

    return fib_sum
