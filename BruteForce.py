
from itertools import permutations
import os
import time
import math
from utils import *


def without_pruning(attributes):

    # best combination
    num_images = len(attributes)
    combination = permutations(range(num_images))
    best_interest_factor = 0
    best_perm = None
    # print(combination)
    for single_perm in combination:
        # single_perm = combination[i]
        # print(single_perm)
        interest_factor = 0
        for j in range(len(single_perm) - 1):
            interest_factor+=compute_interest_factor(attributes[single_perm[j]], attributes[single_perm[j+1]])
            # find out the max interest factor and slides(photo combination)
        if interest_factor > best_interest_factor:
            best_interest_factor = interest_factor
            best_perm = single_perm
    # open file for writing in utf-8 encoding type
    # fp = open("Slideshow.txt", "w", encoding="utf-8")
    #
    # fp.write((str(len(photos))))
    # fp.write("\n")
    #
    # for i in range(len(photos)):
    #     fp.write(str(slides[i]))
    #     fp.write("\n")
    #
    # fp.close()

    return best_interest_factor, best_perm
