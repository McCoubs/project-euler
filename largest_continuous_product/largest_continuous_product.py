def largest_continuous_product(series, adjacent):
    """
    Function returns the largest product of adjacent numbers within the given series.

    REQ: type(series) == str and int(series)
    REQ: type(adjacent) == int

    :param series: {string} series of whole integers within a string
    :param adjacent: {int} number of adjacent ints to multiply within series
    :return: the largest product of adjacent integers within series
    """

    # check input, raise relevant errors
    if type(adjacent) != int or type(series) != str:
        raise TypeError("One of input params was not correct type")
    if adjacent < 0:
        raise ValueError("Input param 'adjacent' was was less than zero")

    # int(series) will raise ValueError if it contains characters other than ints
    try:
        int(series)
    except ValueError:
        raise ValueError("Series contained characters that were not ints")

    # if adjacent is larger than len of series, set adjacent = len(series)
    adjacent = len(series) if adjacent > len(series) else adjacent

    # loop through entire series
    largest_product = 0
    for i in range(0, len(series) - adjacent + 1):
        curr_product = 1
        # if current splice does not contain 0, get product
        if "0" not in series[i:i + adjacent]:
            # loop through adjacent number of ints, getting product of adjacent ints
            for j in range(i, i + adjacent):
                curr_product *= int(series[j: j + 1])
        # else skip calculations to reduce computation time
        else:
            curr_product = 0
        # if current product is larger than stored product, store it
        if curr_product > largest_product:
            largest_product = curr_product

    return largest_product
