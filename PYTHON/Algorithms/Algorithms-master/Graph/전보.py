import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, idx = heapq.heappop(q)

        if distance[idx] < dist:
            continue

        for i in graph[idx]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)
# print(distance)

max_value = 0
cnt = 0
for i in distance:
    if i != INF:
        cnt += 1
        max_value = max(i, max_value)

print(cnt-1, max_value)



# 3 2 1
# 1 2 4
# 1 3 2