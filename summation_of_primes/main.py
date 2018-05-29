import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from summation_of_primes import summation_of_primes


if __name__ == "__main__":

    # get input from user
    limit = input("Please enter the limit to sum until: ")
    # call func with input
    try:
        summation = summation_of_primes(int(limit))
        # output info to user
        print("The sum of all primes up to and including {} is: {}".format(limit, summation))
    except TypeError as error:
        print(error.args)
