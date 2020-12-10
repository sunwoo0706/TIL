n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

from bisect import bisect_left, bisect_right
# 반복문으로 구현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return None

for i in range(m):
    if binary_search(a, b[i], 0, n-1) != None:
        print('yes')
    else:
        print('no')