#!/bin/python3

import math
import os
import random
import re
import sys


def maxShared(friends_nodes, friends_from, friends_to, friends_weight):
    # Write your code here
    answer = 0
    arr = [[0] * friends_nodes for _ in range(friends_nodes)]
    intrerest = [[] for _ in range(max(friends_weight))]
    d = dict()
    print(friends_to)

    print(len(friends_from))
    for i in range(len(friends_from)):
        print(friends_from[i], friends_to[i])
        if(friends_from[i] < friends_to[i]):
            tmp = friends_from[i]
            friends_from[i] = friends_to[i]
            friends_to[i] = tmp

    print(friends_to)
    print(friends_from)

    for i in range(len(friends_from)):
        # tuple t = (riends_from[i],friends_to[i])
        if (friends_from[i],friends_to[i]) in d.keys():

            d[(friends_from[i],friends_to[i])] += 1
        else:
            d[(friends_from[i],friends_to[i])] = 1
        # arr[friends_from[i]-1][friends_to[i]-1]+=1

    print("max d", max(d))
    d_max = 0
    for em in d:
        if(d_max < d[em]):
            d_max = d[em]
    print(d_max)

    for i in range(len(friends_weight)):
        if (d[(friends_from[i],friends_to[i])] == d_max):
            intrerest[friends_weight[i]-1].append((friends_from[i], friends_to[i]))
    print(arr)

    m = len(intrerest[0])
    idx = 0
    for i in range(len(intrerest)):
        if m < (len(intrerest[i])):
            m = len(intrerest[i])
            idx = i

    max_interest = (intrerest[idx])
    mul = []
    for em in max_interest:
        mul.append(em[0] * em[1])

    print(d)
    print(intrerest)
    print(max_interest)
    answer = max(mul)

    # for i in range(len(friends_from)):
    #     arr[friends_from[i]-1][friends_to[i]-1] = friends_weight[i]

    # print(arr)
    # for i in range(len(friends_weight)):
    #     temp = []
    #     temp.append(friends_from[i])
    #     temp.append(friends_to[i])
        
    #     intrerest[friends_weight[i]-1].append(temp)

    return answer

friends_nodes = 4
friends_edges = 5
friends_from = [1,1,2,2,2]
friends_to = [2,2,3,3,4]
friends_weight = [1,2,1,3,3] 
if __name__ == '__main__':

    friends_nodes, friends_edges = map(int, input().rstrip().split())

    friends_from = [0] * friends_edges
    friends_to = [0] * friends_edges
    friends_weight = [0] * friends_edges

    for i in range(friends_edges):
        friends_from[i], friends_to[i], friends_weight[i] = map(int, input().rstrip().split())

    result = maxShared(friends_nodes, friends_from, friends_to, friends_weight)


print(maxShared(friends_nodes, friends_from, friends_to, friends_weight))