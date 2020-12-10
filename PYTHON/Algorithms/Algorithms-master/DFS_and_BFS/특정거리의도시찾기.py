from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = 4 # 도시의 개수
M = 4 # 도로의 개수
K = 2 # 거리정보(최단거리)
X = 1 # 출발도시
graph = [[], [2, 3], [3, 4], [], []]

distance = [-1] * (N+1)
distance[X] = 0


def bfs():
    queue = deque([X])
    while queue:
        now = queue.popleft()
        for next_node in graph[now]:
            if distance[next_node] == -1:
                distance[next_node] = distance[now] + 1
                queue.append(next_node)

bfs()
chk = False
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        chk = True

if chk == False:
    print(-1)