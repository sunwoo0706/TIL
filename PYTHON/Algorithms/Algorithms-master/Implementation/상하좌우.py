# 시뮬레이션 유형 : 명령에 따라서 요구사항대로 차례로 구현하면 됨
n = 5
plans = ['R', 'R', 'R', 'U', 'D', 'D']
x, y = 1, 1

dx = [0, 0, -1, 1] # LRUD
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny

print(x, y)