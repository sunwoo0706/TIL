# https://programmers.co.kr/learn/courses/30/lessons/43238?language=python3
# 다시 풀어보기


# 입국심사를 기다리는 사람 수 n
# 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times
# 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 


def solution(n, times):
    start, end = 0, max(times) * n

    while start <= end:
        mid = (start + end) // 2
        # 가능한경우는 end = mid - 1
        if sum([mid // x for x in times]) >= n:
            end = mid - 1
        # 불가능한경우는 start = mid + 1
        else:
            start = mid + 1

    return start



n = 6
times = [7, 10]	
print(solution(n, times))