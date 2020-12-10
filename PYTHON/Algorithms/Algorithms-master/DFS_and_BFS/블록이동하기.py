# 2020 카카오 신입 공채 1차
# 0은 빈칸, 1은 벽 (로봇은 벽으로 이동 못함)
# 목적지 까지 가는데 최소 시간 구하기 = bfs

from collections import deque

def solution(board):
    q = deque([[(0,0), (0,1), 0]]) # 로봇의 좌표(로봇은 처음에 (0,0) (0,1))
    
    n = len(board)
    
    v = []
    
    while q:
        robot = q.popleft()
        
        
        l = robot[0] # x:l[0], y:l[1]
        r = robot[1]
        time = robot[2]
        # print(l, r, time)

        # 블록 밖 넘어갔을 때
        if l[0] < 0 or l[0] >= n or l[1] < 0 or l[1] >= n or r[0] < 0 or r[0] >= n or r[1] < 0 or r[1] >= n:
            continue

        v = []
        v.append([l, r])
        # print('v', v)
        # print(robot, q)

        
        if l == (n-1, n-1) or r == (n-1, n-1): 
            return time
        
        for nxt in move(l, r, board):
            # print(nxt, v)
            if nxt not in v:
                nxt.append(time+1)
                q.append((nxt))
                # print('q', q)
                
                v.append(nxt)
                # print('v', v)

        
        

    return time

def move(l, r, board):
    # 상하좌우 반시계방향으로 회전시키는 좌표들
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    n = len(board)

    v = []
    # 회전 및 상하좌우로 이동하면서 탐색한다.
    for i in range(4): # 상하좌우 이동
        k = [(l[0]+dx[i], l[1]+dy[i]), (r[0]+dx[i], r[1]+dy[i])]
        if k[0][0] < 0 or k[0][0] >= n or k[0][1] < 0 or k[0][1] >= n or k[1][0] < 0 or k[1][0] >= n or k[1][0] < 0 or k[1][0] >= n:
            continue
        if board[k[0][0]][k[0][1]] == 0 and board[k[1][0]][k[1][0]] == 0 and k not in v:
            # q.appendleft(k)
            v.append(k)

    for i in range(4): # 왼쪽회전 4개, 왼쪽은 고정
        k = [(l[0], l[1]), (l[0]+dx[i], l[1]+dy[i])] 
        
        s = (l[0]+dx[i] + r[0], l[1]+dy[i] + r[1]) #회전축이 1인지 검사하기 위해서 
        if s[0] < 0 or s[0] >= n or s[1] < 0 or s[1] >= n or k[0][0] < 0 or k[0][0] >= n or k[0][1] < 0 or k[0][1] >= n or k[1][0] < 0 or k[1][0] >= n or k[1][0] < 0 or k[1][0] >= n:
            continue
        if board[s[0]][s[1]] == 1:
            continue
    
        if board[k[0][0]][k[0][1]] == 0 and board[k[1][0]][k[1][0]] == 0 and k not in v:
            # q.appendleft(k)
            v.append(k)

    for i in range(4): # 오른쪽 회전 4개
        k = [(r[0] + dx[i], r[1] + dy[i]), (r[0], r[1])] 
        s = (r[0]+dx[i] + l[0], r[1]+dy[i] + l[1]) #회전축이 1인지 검사하기 위해서 
        if s[0] < 0 or s[0] >= n or s[1] < 0 or s[1] >= n or k[0][0] < 0 or k[0][0] >= n or k[0][1] < 0 or k[0][1] >= n or k[1][0] < 0 or k[1][0] >= n or k[1][0] < 0 or k[1][0] >= n:
            continue
        if board[s[0]][s[1]] == 1:
            continue
    
        if board[k[0][0]][k[0][1]] == 0 and board[k[1][0]][k[1][0]] == 0 and k not in v:
            # q.appendleft(k)
            v.append(k)

    return v

board = [[0,0,1],[0,0,0],[0,0,0]]
board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
# print(solution(board))
