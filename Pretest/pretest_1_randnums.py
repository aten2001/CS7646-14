## Write a program to generate 100 random integers between 1 and 100. It should
#   generate exactly the same numbers each time you run it.
#   Bonus: If you wonder whether the distribution should be
#   normal or uniform, give yourself extra points.

## import
import os
import sys
path_to_anaconda = "./"
sys.path.append(path_to_anaconda)
import random
import numpy

## set random seed
def seededRandNumGen():
    random.seed(1)
    rand_nums = random.sample(xrange(1, 101), 100)
    return rand_nums

seededRandNumGen()

