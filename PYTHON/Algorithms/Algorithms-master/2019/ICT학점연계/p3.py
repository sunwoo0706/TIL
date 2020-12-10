#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minX(arr):
    # Write your code here
    x = 1
    if(arr[0] < 0):
    	x = -(arr[0]) + 1

    answer = x
    temp = []
    for i in range(len(arr)):
    	answer += arr[i]
    	if(answer < 0):
    		temp.append(answer)

    
    if(temp != []):
	    p = min(temp)
	    x = x + abs(p) + 1

    return x




# arr = [6, 1, 3, 7, 4, 6, 4, 3]
# arr = [6, 1, 3]
# # arr = [6, 1, 3]
arr = [-2, 3, 1, -5]
# arr = arr = [-5, 4, -2, 3, 1, -1, -6, -1, 0, 5]
arr = [-5, 4, -2, 3, 1, -1, -6, -1, 0, -5]
arr = [-5, 4, -2, 3, 1]
arr = [-5, 4, -2, 3, 1, -1, -6, -1, 0, 5]
print(minX(arr))