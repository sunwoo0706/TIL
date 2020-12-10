# 사이클이 없는 방향그래프(DAG)의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것
# 여러가지 답이 존재

from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1) # 진입차수
graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) 
    indegree[b] += 1 

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    print(result)

topology_sort()

# 7 8
# 1 2
# 1 5
# 2 3 
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4