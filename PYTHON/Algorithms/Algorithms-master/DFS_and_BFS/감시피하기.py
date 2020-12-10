# https://www.acmicpc.net/problem/18428
# 선생님, 학생, 장애물로 구성
# 장애물을 3개 설치해서 선생님으로부터 감시를 피할 수 있는지 검사(yes or no)

import copy
from collections import deque



n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(str, input().split())))

# n = 5
# arr = [['X', 'S', 'X', 'O', 'T'],['T', 'O', 'S', 'X', 'X'], ['X', 'X', 'O', 'X', 'X'], ['X','T', 'X', 'X', 'X'],['X', 'X', 'T', 'X', 'X']]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

t = []
answer = 'NO'

# 선생님들 위치 튜플로 만들기
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'T':
            t.append((i, j))

# 장애물 설치 (dfs)
def obstacle(start, cnt):
    # 가능한 3가지 빈공간에서 3가지 경우를 다 본다.
    # 그리고나서 선생님 감시를 위한 dfs를 돌린다. 
    # bfs 리턴값이 1이면(모든 학생들이 다 감시를 피하면) => 이함수를 리턴하고 yes를 출력한다.
    # 아니면 다른 장애물을 설치한다.
    # 다른 가능한 장애물을 모두 설치했는데도 실패하면, no를 출력한다.
    global answer

    # 3개의 장애물을 모두 설치했을 때
    if cnt == 3:
        
        a = copy.deepcopy(arr)
        # bfs 돌려서 선생님이 감시하도록 한다.
        res = bfs(a)
        if res == True:
            answer = 'YES'
        return

    # 아직 3개의 장애물을 설치하지 않았을 때
    for i in range(start, n*n):
        x = i // n
        y = i % n

        if arr[x][y] == 'X':
            arr[x][y] = 'O' # O로 바꾸고
            obstacle(i+1, cnt+1)
            arr[x][y] = 'X' # 모두 설치했으면 댜른 장애물을 설치하기 위해 다시 X로 바꾼다.

    

# 선생님이 학생들을 상하좌우로 감시 (dfs 돌면서 수행)
def bfs(a):
    q = deque(t) # 선생님이 있는 좌표 리스트를 deque로 바꿈
    while q:
        x, y = q.popleft() # x, y 좌표 뽑아서
        # 선생님은 상하좌우로 탐색한다. 
        # 단, 상하좌우, 상하좌우 이렇게 탐색하는게 아님.. 쭉~ 상으로만 탐색, 하로만 탐색 이런식
        for i in range(4):
            chk = 0
            nx = x
            ny = y
            
            while chk == 0 and not (nx+dx[i] < 0 or nx+dx[i] >=n or ny+dy[i] < 0 or ny+dy[i] >= n):
                nx += dx[i]
                ny += dy[i]
                # O 발견하면 해당 선생님은 탐색 중지해야한다.
                if a[nx][ny] == 'O':
                    chk = 1
                
                # 탐색하다가 S 발견하면 리턴 (한명의 학생이 통과하지 못한 경우)
                if a[nx][ny] == 'S':
                    return False

            
    # 모든 학생이 통과한 경우
    return True

obstacle(0, 0)
print(answer)
