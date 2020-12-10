# 삼성전자 SW 역량테스트
from collections import deque

n, l, r = map(int, input().split()) 
# nxn 행렬 입력받기 (나라는 총 nxn 개이다.)
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
chk = 0

# bfs로 인접한 애들의 인구 차이를 구한다.
def bfs(x, y):
    move_q = deque()
    q.append((x, y))
    visited[x][y] = 1
    people, cnt = 0, 0

    # bfs로 인접한 애들의 인구 차이를 구한다.
    while q:
        x, y = q.popleft()
        move_q.append((x, y))
        people += graph[x][y]
        cnt += 1 

        # 상하좌우로 자신이랑 인접한 애들의 diff 를 구한다.
        for i in range(4): 
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            diff =  abs(graph[x][y] - graph[nx][ny])
            if visited[nx][ny] == 0 and diff >= l and diff <= r:
                # 큐에 넣고 방문처리
                q.append((nx, ny)) 
                visited[nx][ny] = cnt

    while move_q:
        x, y = move_q.popleft()
        graph[x][y] = people // cnt
    # print(graph)
    if cnt == 1:
        return 0

    return 1
    

# 인구이동이 없을때까지 계속 인구이동을 진행한다.
res = 0
while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    q = deque()
    cnt = 0
    for i in range(n):
        for j in range(n):      
            cnt += bfs(i, j)
    
    if cnt == 0:
       break

    res += 1

print(res)

