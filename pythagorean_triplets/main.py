import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pythagorean_triplets import pythagorean_triplets


if __name__ == "__main__":

    # get input from user
    triplet_sum = input("Please enter the triplet sum: ")
    # call func with input
    try:
        triplets = pythagorean_triplets(int(triplet_sum))
        # output info to user
        print("The pythagorean triplets of {} are: a={} b={} c={} and abc={}".format(
            triplet_sum, triplets["a"], triplets["b"], triplets["c"], triplets["abc"]))
    except (TypeError, ValueError) as error:
        print(error.args)
