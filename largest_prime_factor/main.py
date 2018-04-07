from largest_prime_factor import largest_prime_factor


if __name__ == "__main__":

    # get inputs form user
    input_num = input("Please enter a number to find its largest prime factor: ")
    # call func with inputs
    lpf = largest_prime_factor(int(input_num))
    # output info to user
    print("The largest prime factor of {} is {}".format(input_num, lpf))
