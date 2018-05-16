import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from find_nth_prime import find_nth_prime


if __name__ == "__main__":

    # get input from user
    nth_prime = input("Please enter the nth prime to return: ")
    # call func with input
    try:
        found_prime = find_nth_prime(int(nth_prime))
        # output info to user
        print("The {} prime in the natural numbers is: {}".format(nth_prime, found_prime))
    except (TypeError, ValueError) as error:
        print(error.args)

