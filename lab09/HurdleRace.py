#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

def hurdleRace(k, height):
    dose = 0 # to count number of dose needed

    for i in height: #for each value i in height
        if i > k: #if height of hurdle > max height
            d = i - k # get the number of dose
            if d > dose:
                dose = d

    return dose 
    

if __name__ == '__main__':

    #get input from user
    #rstrip removes trailing whitespaces
    #split string into substrings
    
    first_multiple_input = input().rstrip().split()

    #assign first element to variable n(number of hurdles)
    #convert string into integer

    n = int(first_multiple_input[0])

        #assign second element to the variable k(max height)
        #convert string into integer

    k = int(first_multiple_input[1])
    
    #get a list of hurdle height
    #remove the trailing whitespaces
    #split strings into substrings
    #convert all values in the list into integer using map()
    #map returns map object

    height = map(int, input().rstrip().split())

    #call hurdleRace() and pass k,height as argument

    result = hurdleRace(k, height)

    print(result)
