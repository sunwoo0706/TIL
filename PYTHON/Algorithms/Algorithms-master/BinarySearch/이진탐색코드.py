# 재귀함수로 구현
def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target: 
        return binary_search(array, target, start, mid-1)    
    else:
        return binary_search(array, target, mid+1, end)


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



# 데이터개수, 범위가 클 경우 이진탐색 사용!
# 시간초과 안받기 위한 입력 사용법
import sys
input_data = sys.stdin.readline().rstrip()


# 이진탐색 라이브러리

from bisect import bisect_left, bisect_right
a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))


# 파라매트릭서치
# 최적화문제를 결정문제(y,n)으로 바꾸어 푸는 문제
# 특정한 조건을 만족하는 가장 알맞는 답을 빠르게 찾기

