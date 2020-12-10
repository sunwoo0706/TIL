# 나이트는 수직2 수평1 or 수평2 수직1
n = 8
x, y = 1, 1

# 가능한 좌표
dx = [-1, -1, 1, 1, -2, 2, -2, 2]
dy = [-2, 2, -2, 2, -1, -1, 1, 1]

result = 0


for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    result += 1

print(result)