import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from smallest_continuous_multiple.smallest_continuous_multiple import smallest_continuous_multiple


if __name__ == "__main__":

    # get inputs form user
    multiple = input("Please enter a number: ")
    # call func with inputs
    smallest_int = smallest_continuous_multiple(int(multiple))
    # output info to user
    print("The smallest int that can be evenly divided by all ints less than or equal to {} is {}".format(
        multiple, smallest_int))
