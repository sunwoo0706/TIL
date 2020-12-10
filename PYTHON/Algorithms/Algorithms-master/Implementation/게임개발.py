# nxm 크기의 직사각행렬 안에서 움직이는 캐릭터

n, m = 4, 4
x, y, direction = 1, 1, 0 # 유저가 (1, 1)에서 북쪽을 바라봄

arr = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
d = [[0]*m for _ in range(n)]

dx = [-1, 0, 1, 0] # 북, 동, 남, 서
dy = [0, 1, 0, -1] 


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]   

    # step 1
    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    
    # step 2
    else:
        turn_time += 1

    # step 3
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if arr[ny][nx] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
