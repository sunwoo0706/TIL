from collections import deque

# 위상정렬!

n = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
cost = [0] * (n+1)

for i in range(1, n+1):
    # 시간 선수과목들 -1 로 input 받기
    data = list(map(int, input().split()))
    cost[i] = data[0] 
    for d in data[1:-1]:
        indegree[i] += 1
        graph[d].append(i)


def topology_sort():
    result = [0] * (n+1)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                cost[i] = cost[i] + cost[now]

    print(cost[1:])
    

topology_sort()



# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1