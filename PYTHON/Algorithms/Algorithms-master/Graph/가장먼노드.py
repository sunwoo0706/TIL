# https://programmers.co.kr/learn/courses/30/lessons/49189

# n개의 노드가 있는 그래프가 있습니다. 
# 각 노드는 1부터 n까지 번호가 적혀있습니다. 
# 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 
# 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

# 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

# 다익스트라 알고리즘 사용

import heapq
def solution(n, edge):
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    distance = [INF] * (n+1)
    start = 1
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    max_cost = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))
                max_cost = cost


    return distance.count(max_cost)
    



n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	

print(solution(n, vertex))