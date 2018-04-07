from helper_methods import least_common_multiple


def sum_of_multiples(maximum, divisor_one, divisor_two):
    """(int, int, int) -> int
    The function takes a maximum and 2 ints. Returns sum of all multiples of divisor_one and divisor_two less
    than or equal to the maximum.

    Uses the principle of summation from 1 to n ( n(n+1)/2 ), therefore the sum of all multiples
    of k to m is ( km(m+1)/2 ), where m is the number of times k goes into the max (n)

    REQ: max, divisor_one, divisor_two >= 1
    REQ: max, divisor_one, divisor_two are whole integers
    """

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
