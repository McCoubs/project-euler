from helper_functions import least_common_multiple


def sum_of_multiples(maximum, divisor_one, divisor_two):
    """
    Function returns sum of all multiples of divisor_one and divisor_two less
    than or equal to the maximum.

    Uses the principle of summation from 1 to n ( n(n+1)/2 ), therefore the sum of all multiples
    of k to m is ( km(m+1)/2 ), where m is the number of times k goes into the max (n).

    REQ: max, divisor_one, divisor_two >= 1
    REQ: type(max, divisor_one, divisor_two) == int

    :param maximum: {int} is maximum int to sum to
    :param divisor_one: {int} is first multiple to sum
    :param divisor_two: {int} is second multiple to sun
    :return: {int} sum of all multiples of divisor_one and divisor_two to maximum
    """

    # check input, raise relevant errors
    if type(maximum) != int or type(divisor_one) != int or type(divisor_two) != int:
        raise TypeError("One of input params was not type of int")
    if maximum <= 0 or divisor_one <= 0 or divisor_two <= 0:
        raise ValueError("One of input params was a negative/zero value")

    # get whole number of times each divisor goes into max
    quotient_one = maximum // divisor_one
    quotient_two = maximum // divisor_two

    # get lcm of divisor_one & divisor_two, as this will be double counted
    lcm = least_common_multiple(divisor_one, divisor_two)
    lcm_quotient = maximum // lcm

    # get divisor and lcm sums
    divisor_one_sum = (divisor_one * quotient_one * (quotient_one + 1)) // 2
    divisor_two_sum = (divisor_two * quotient_two * (quotient_two + 1)) // 2
    lcm_sum = (lcm * lcm_quotient * (lcm_quotient + 1)) // 2

    # add quotient sums and subtract lcm sum
    return divisor_one_sum + divisor_two_sum - lcm_sum
