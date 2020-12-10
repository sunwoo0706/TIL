# 이것이 코딩테스트다 - 그리디
# 2019 SW 마에스트로

from itertools import combinations

n, m = map(int, input().split())
weight = list(map(int, input().split()))

print(sum(list(map(lambda x: x[0] != x[1], list(combinations(weight, 2))))))
