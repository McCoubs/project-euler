def summation(limit):
    """
    Returns the summation of all natural numbers from 0 to limit

    Uses short form summation formula natural summation

    :param limit: {int}
    :return: {int}
    """

    return (limit * (limit + 1)) // 2 if limit >= 0 else 0


def square_summation(limit):
    """
    Returns the summation of all squared natural numbers from 0 to limit

    Uses the short form summation formula for summation of squares

    :param limit: {int}
    :return: {int}
    """

    return (limit * (limit + 1) * (2 * limit + 1)) // 6 if limit >= 0 else 0
