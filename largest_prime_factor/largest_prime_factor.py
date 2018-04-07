def largest_prime_factor(input_num):
    """
    Function returns the largest prime factor of an input.

    REQ: input_num >= 0 and whole

    :param input_num: {int} is original input number
    :return: {int} the largest prime factor of the input
    """

    # set current lowest prime to lowest prime factor (2)
    curr_lpf = 2
    # loop while our current input is greater than our current lpf
    while input_num > curr_lpf:
        # if division results in whole number, divide input by curr_lpf and reset to 2
        if input_num % curr_lpf == 0:
            input_num = input_num // curr_lpf
            curr_lpf = 2
        # else move onto next largest factor
        else:
            curr_lpf += 1
    return curr_lpf
