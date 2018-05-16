import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sum_square_difference import sum_square_difference


if __name__ == "__main__":

    # get input from user
    limit = input("Please enter the limit to sum until: ")
    # call func with input
    try:
        square_difference = sum_square_difference(int(limit))
        # output info to user
        print("The difference between the sum of the squares and the square of the sum up to the given limit is {}".
              format(square_difference))
    except (TypeError, ValueError) as error:
        print(error.args)
