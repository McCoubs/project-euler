import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from largest_continuous_product import largest_continuous_product


if __name__ == "__main__":

    # get inputs form user
    series = input("Please enter a series of numbers to check: ")
    adjacent = input("Please enter number of adjacent numbers to multiply: ")
    try:
        # call func with inputs
        product = largest_continuous_product(series, int(adjacent))
        # output info to users
        print("The largest product in the given series is: {}".format(product))
    except (TypeError, ValueError) as error:
        print(error.args)
