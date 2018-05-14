def sum_square_difference(limit):
    """
    Function returns difference between the sum of the squares up to and including limit and the square of the
    sum up to and including limit.

    Uses the principle of summation from 1->n of n = ( n(n+1) // 2 ) and 1->n of n^2 = ( n(n + 1)(n + 2) // 6 )

    REQ: limit >= 1 and type(limit) == int

    :param limit: {int} is limit to sum until
    :raises {ValueError} if input < 0
    :raises {TypeError} if type(limit) != int
    :return: {int}
    """

    # check input, raise relevant errors
    if type(limit) != int:
        raise TypeError("Input param 'limit' was not type of int")
    if limit < 0:
        raise ValueError("Input param 'limit' was a negative value")

    # get square of sum to limit
    square_of_sum = pow((limit * (limit + 1)) // 2, 2)
    # get sum of squares to limit
    sum_of_squares = (limit * (limit + 1) * (2 * limit + 1)) // 6

    # return difference
    return square_of_sum - sum_of_squares
