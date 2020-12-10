# https://programmers.co.kr/learn/courses/30/lessons/42628

# 이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 
# 모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.

 
import heapq

def solution(operations):
    h = []
    for i, x in enumerate(operations):
        if x.startswith('I'):
            heapq.heappush(h, int(x.split()[1]))

        if x.startswith('D') and h:
            if x == "D -1": # 최소힙
                heapq.heappop(h)

            elif x == "D 1": # 최대힙
                h.remove(max(h))
        
    if h:
        return [max(h), min(h)]
    
    return [0, 0]
    


operations = ["I 16","D 1"]	
operations = ["I 7","I 5","I -5","D 1"]	
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

print(solution(operations))