# https://programmers.co.kr/learn/courses/30/lessons/42578

from collections import Counter
from functools import reduce

def solution(clothes):
    c = Counter(x[1] for x in clothes)
    print(c)
    # ex. (a + 1)(b + 1)(c + 1) - 1 = (a + b + c) + (ab + bc + ca) + abc
    r = reduce(lambda x, y: x*y, [x+1 for x in c.values()]) - 1 # 아무것도 안입은경우 뺴주기
    return r
    

    # p = list(permutations(d))
    # print(p)

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
# clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	
print(solution(clothes))