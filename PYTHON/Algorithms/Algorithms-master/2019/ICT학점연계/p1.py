
import math
import os
import random
import re
import sys



#
# Complete the 'collision' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY speed
#  2. INTEGER pos
#

def collision(speed, pos):
    print("speed", speed)
    print("pos", pos)
    # Write your code here
    n = len(speed)

    # print(speed)
    # print(len(speed))

    # arr = [[0 for col in range(pos+1)] for row in range(n)]
    arr = [0 for _ in range(n)]

    # for i in range(n):
    #     for j in range(pos+1):
    #         arr[i][j] = i + speed[i] * j
    answer = 0
    for i in range(n):
        arr[i] = i + speed[i]

    print(arr)

    for i in range(0, pos):
        # print(prime_factor(arr[pos]), (arr[i]))
        print((arr[i],arr[pos]))
        if((arr[i]-arr[pos]) >= 0 and arr[i] >= arr[pos]):
            print(i)
            answer += 1

    # print(answer)
    for i in range(pos+1, n):
        # print(prime_factor(arr[pos]), (arr[i]))
        # print((arr[i])%prime_factor(arr[pos]) == 0 and arr[i] <= arr[pos])
        print((arr[i],arr[pos]))
        if((arr[pos] + i) >= arr[i] and arr[i] <= arr[pos]):
            print(i)
            answer += 1


    # print(answer)
    return answer

def prime_factor(num):
    a = []
    factor=2
    min_factor = 2;
    while not num == 1:
        if num%factor == 0:
            # print(num,factor)
            num = num/factor

            a.append(factor)
        else:
            factor+=1
    # print(a)
    return min(a)
 


# speed = [6, 6, 1, 6, 3, 4, 6, 8]
speed = [8, 3, 6, 3, 2, 2, 4, 8, 1, 6]
speed = [6, 6, 1, 6,3, 4, 6, 8]
speed = [21, 41, 18, 18, 13, 49, 34, 49, 24, 47, 15, 10, 34, 41, 17, 27, 24, 10, 46, 26, 28, 49, 18]
# speed = [1, 3, 7, 4, 6, 4]
# speed = [6, 6, 1, 6, 3, 4, 6, 8]
pos = 3

# 7
# if __name__ == '__main__':

#     speed_count = int(input().strip())

#     speed = []

#     for _ in range(speed_count):
#         speed_item = int(input().strip())
#         speed.append(speed_item)

#     pos = int(input().strip())

#     result = collision(speed, pos)


print(collision(speed, pos))
