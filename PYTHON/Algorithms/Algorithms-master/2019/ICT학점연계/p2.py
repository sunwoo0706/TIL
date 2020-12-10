#
# Complete the 'maxDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY nums as parameter.
#
import math
import os
import random
import re
import sys


def maxDifference(nums):
    try:
        # Write your code here
        answer = 0
        arr = []

        for i in range(len(nums)):
            temp = []
            for j in range(0, i):
                if(nums[i] > nums[j]):
                    temp.append(nums[i] - nums[j])
            if(temp != []):
                arr.append(max(temp))
            

        if(arr == []):
            answer = -1
        else:
            answer = max(arr)

        return answer
    except:
        return -1
    

arr = [6, 1, 3, 7, 4, 6, 4, 3]
# arr = [6, 1, 3]
print(maxDifference(arr))