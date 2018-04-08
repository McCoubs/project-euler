from helper_functions import factors


def smallest_continuous_multiple(max_multiple):
    """
    Function takes an int, and returns the smallest natural number evenly divisible by all numbers
    less than or equal to the input max_multiple.

    REQ: max_multiple >= 0 and whole

    :param max_multiple: {int}
    :return: smallest natural number evenly divisible by all number less than or equal to input

    Function reduces time complexity by iteratively removing redundant factors from the
    check_list, ie. suppose 12 exists in the list, then 6, 4, 3, 2 and 1 will have been removed.
    This check is done to remove the factors of every int, to reduce the lookup time later.
    """

    # all numbers less than or equal to 2 are evenly divisible by themselves and below
    if max_multiple <= 2:
        return max_multiple

    check_list = []
    # make a list of all ints from 1 to input
    for i in range(max_multiple):
        check_list.append(i + 1)

    # loop through check list backwards
    for i in reversed(check_list):
        # get factors of i without i included
        temp_factors = factors(i)
        temp_factors.remove(i)
        # loop through the remaining factors, removing them from the check_list
        for j in temp_factors:
            try:
                check_list.remove(j)
            except ValueError:
                pass

    temp_num = max_multiple
    # loop indefinitely until find smallest int that that satisfies exit condition
    while True:
        # if all factors less than max_multiple divide evenly into curr, return
        if all(temp_num % n == 0 for n in check_list):
            return temp_num
        else:
            temp_num += max_multiple
