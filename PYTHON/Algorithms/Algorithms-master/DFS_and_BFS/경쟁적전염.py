from collections import deque

s = 2
x, y = (3, 2)
n, k = (3, 3) # nxn 행렬, k=바이러스 종류
matrix = [[1,0,3],[0,0,0],[2,0,0]]
# virus = [[] for _ in range(k+1)]
virus = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



# k가지 바이러스들 리스트
def get_virus():
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                virus.append((i, j, matrix[i][j]))

    virus.sort(key=lambda v: v[2])

get_virus()    

# virus 퍼트리기 (dfs 사용)
def spred_virus(x, y, t):
    print(x, y, t)
    
    
    # 제한시간 넘어가면
    if t > s: 
        return

    # 상하좌우 dfs 돌리기
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        # 범위 벗어나면 return
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if matrix[nx][ny] == 0:
            matrix[nx][ny] = matrix[x][y]

        spred_virus(nx, ny, t+1)
        


# s 초만큼 바이러스 퍼트리기
for v in range(len(virus)):
    spred_virus(virus[v][0], virus[v][1], 1)
    print()


print('matrix', matrix)
print(matrix[x-1][y-1])