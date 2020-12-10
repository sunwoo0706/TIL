# https://www.acmicpc.net/problem/18406
# 이것이 코딩테스트다

n = list(map(int, input()))

if sum(n[:len(n)//2]) == sum(n[len(n)//2:]):
    print("LUCKY")
else:
    print("READY")