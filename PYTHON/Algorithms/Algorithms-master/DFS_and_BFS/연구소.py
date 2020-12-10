# 삼성전자 SW 역량테스트

import copy
lab = [
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 2],
    [1, 1, 1, 0, 0, 2],
    [0, 0, 0, 0, 0, 2],
]

n = 4
m = 6
virus_list = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_value = 0

# virus 퍼뜨리기
def dfs(x, y, clab):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if clab[nx][ny] == 0:
            clab[nx][ny] = 2
            dfs(nx, ny, clab)

# 벽 선택하기
def wall(start, cnt):
    global max_value
    # 3개의 벽이 모두 선택된 경우
    if cnt == 3:
        clab = copy.deepcopy(lab)
        # print(clab, getSafeArea(clab))
        for i in range(len(virus_list)):
            (x, y) = virus_list[i]
            dfs(x, y, clab)
        print(clab, getSafeArea(clab))
        max_value = max(max_value, getSafeArea(clab))
        return
    
    # 아직 3개의 벽이 선택되지 않은 경우 선택하기
    for i in range(start, n*m):
        x = i // m
        y = i % m

        if lab[x][y] == 0:
            lab[x][y] = 1
            wall(i+1, cnt+1)
            lab[x][y] = 0

# 안전지역 구하기
def getSafeArea(clab):
    result = 0
    for i in range(n):
        for j in range(m):
            if clab[i][j] == 0:
                result += 1
    return result

# virus list 채우기
for i in range(n):
    for j in range(m):
        if lab[i][j] == 2:
            virus_list.append((i, j))

wall(0, 0)


print(max_value)