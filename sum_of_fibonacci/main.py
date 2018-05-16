import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sum_of_fibonacci import sum_of_fibonacci


if __name__ == "__main__":

    # get inputs form user
    maximum = input("Please enter a maximum number: ")
    # default to even
    sum_even = input("Would you lie to sum even or odd terms? ") != "odd"
    # call func with inputs
    term_sum = sum_of_fibonacci(int(maximum), sum_even)
    # output info to user
    print("The sum of all {} terms less than or equal to {} is {}".format("even" if sum_even else "odd",
                                                                          maximum, term_sum))
