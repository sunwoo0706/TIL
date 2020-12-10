# https://www.acmicpc.net/problem/3190
# 삼성 SW 역량테스트
# 구현

# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.
from collections import deque
n = int(input()) # 보드의 크기 = nxn
k = int(input()) # 사과개수

apples = set()
for _ in range(k):
    x, y = map(int, input().split())
    apples.add((x-1, y-1))

l = int(input()) # 뱀의 방향 변환 횟수

change = {}
for _ in range(l):
    x, y = input().split()
    change[int(x)] = y


t = 0
x, y = 0, 0
visited = deque([(y, x)])
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
i = 0
while x < n and y < n and x >= 0 and y >= 0:
    if t in change.keys():    
        if change[t] == 'L':
            if i == 0:
                i = 3
            else:
                i -= 1
        elif change[t] == 'D':
            if i == 3:
                i = 0
            else:
                i += 1
    x += dx[i]
    y += dy[i]
    t += 1
    
    if (y, x) in visited: # 자기 자신이랑 닿은경우
        break
    
    if (y, x) not in apples: # 사과에 있는 경우 빼주기
        visited.popleft()
    else:   
        apples -= {(y, x)}

    visited.append((y, x))

    
print(t)
    