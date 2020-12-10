# https://programmers.co.kr/learn/courses/30/lessons/42626

# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수(가장 낮은거) + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
# Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

import heapq

def solution(scoville, k):
    heapq.heapify(scoville)

    t = 0
    while len(scoville) >= 2:
        t += 1

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new = first + second * 2
        heapq.heappush(scoville, new)

        third = heapq.heappop(scoville)
        if min(new, third) >= k:
            return t
        else:
            heapq.heappush(scoville, third)
            
    return -1
    



scoville = [1, 2, 3, 9, 10, 12]	
K = 7

print(solution(scoville, K))