import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sum_of_multiples import sum_of_multiples


if __name__ == "__main__":

    # get inputs form user
    maximum = input("Please enter a maximum number: ")
    divisor_one = input("Please enter your first multiple: ")
    divisor_two = input("Please enter your second multiple: ")
    try:
        # call func with inputs
        multiple_sum = sum_of_multiples(int(maximum), int(divisor_one), int(divisor_two))
        # output info to user
        print("The sum of all multiples of {} and {} less than or equal to {} is {}".format(divisor_one, divisor_two,
              maximum, multiple_sum))
    except (TypeError, ValueError) as error:
        print(error.args)
