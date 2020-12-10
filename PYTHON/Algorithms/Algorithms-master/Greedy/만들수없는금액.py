# 이것이 코딩테스트다
# N개의 동전을 이용해 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하시오

n = 5
# arr = list(map(int, input().split()))
arr = [3, 2, 1, 1, 9]


arr.sort()

target = 1
for x in arr:
    print(target, x)
    if target < x:
        break
    target += x

print(target)
