from collections import deque

# 최단거리 = 큐를 활용!
# 간선의 비용이 같다 = bfs
# 간선의 비용이 다르다 = 다익스트라

n, m = (5, 6)
graph = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]

# 상하좌우 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y): # 큐
    queue = deque()
    queue.append((x, y))

    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft() # 큐에서 원소를 꺼낼 떄 사용
        # 상하좌우로 보기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 
                queue.append((nx, ny))
    
    return graph[n-1][m-1]

        


print(bfs(0, 0))