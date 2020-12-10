# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    total_weight = truck_weights[0] # 다리 안에 있는 트럭들의 총 무게
    truck_weights = deque(truck_weights) # 다리를 아직 지나지 않은 트럭들
    q = deque([truck_weights.popleft()]) # 다리에 있는 트럭들
    t = 0
    while q: # 다리에 있는 트럭들이 있으면
        t += 1
        if len(q) == bridge_length: # 다리에 있는 트럭들의 개수가 꽉 차면
            total_weight -= q.popleft()

        if not truck_weights: # 다리를 아직 지나지 않은 트럭이 없으면 break
            break

        if total_weight + truck_weights[0] <= weight: # 새로운 트럭의 무게가 안넘어가면
            p = truck_weights.popleft()
            total_weight += p
            q.append(p)
        else: # 무게 넘어가면 일단 0으로 채우고 다시 루프 돌기
            q.append(0)

    return t + bridge_length



bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]	

# bridge_length = 100
# weight = 100
# truck_weights = [10]
# truck_weights = [10,10,10,10,10,10,10,10,10,10]	

print(solution(bridge_length, weight, truck_weights))