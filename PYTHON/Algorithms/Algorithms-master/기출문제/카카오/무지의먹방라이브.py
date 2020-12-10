# https://programmers.co.kr/learn/courses/30/lessons/42891
# 2019 카카오 신입공채

# 풀이) 그리디 - 정확성o, 효율성o
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i, x in enumerate(food_times):
        heapq.heappush(q, (x, i+1))
    
    sum_value = 0 # 먹기위해 사용한시간
    previous = 0 # 직전에 다 먹은 음식시간 
    length = len(food_times) # 남은 음식의 개수

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]

# 풀이) 구현 - 정확성o, 효율성x
def solution(food_times, k):
    i = 0 # 초
    cur = 0
    if sum(food_times) <= k:
        return -1
    while True:
        if cur >= len(food_times):
            cur = 0
            continue 
        if food_times[cur] == 0:
            cur += 1    
            continue

        if i >= k:
            return cur+1
        
        food_times[cur] -= 1
        cur += 1
        i += 1
        
    return -1

import heapq
food_times = [3, 1, 2]	
k = 5

food_times = [4, 6, 8]
k = 15
print(solution(food_times, k))
