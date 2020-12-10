# https://programmers.co.kr/learn/courses/30/lessons/42861

# n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 
# 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때, 필요한 최소 비용을 return 하도록 solution
# 다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.
# 같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
# 모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.

def solution(n, costs):
    costs.sort(key=lambda x:x[2])
    print(costs)
    completed = set()
    answer = 0
    completed.add(0)
    while len(completed) < n:
        for x, y, cost in costs:
            if x in completed or y in completed:
                if x in completed and y in completed:
                    print(x, y, cost)
                    continue # x, y 둘다 있으면 다음으로 넘어가서 검사
                else:
                    completed.add(x)
                    completed.add(y)
                    answer += cost
                    break # 이게 중요..ㅎ for 문을 빠져나와서 cost 처음부터 검사한다..ㅎ
            print('t1', completed, x, y, cost) 
        print('t2', completed)

    return answer

n = 6
costs = [[0,1,1],[0,2,10],[1,2,5],[3, 5,1],[4, 5, 3],[2,5,8],[2,3,11]]	

# n = 4
# costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	
print(solution(n, costs))

# content-based matching에 대한 슬라이드 보강