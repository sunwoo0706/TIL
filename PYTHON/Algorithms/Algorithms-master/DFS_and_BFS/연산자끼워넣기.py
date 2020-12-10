# 삼성전자 SW 역량테스트
# https://www.acmicpc.net/problem/14888


from itertools import permutations
from collections import deque

# n = 2
# arr = [5, 6]
# op_cnt = [0, 0, 1, 0] # + - x / 개수

# n = 3
# arr = [3, 4, 5]
# op_cnt = [1, 0, 1, 0] # + - x / 개수

# n = 6
# arr = [1, 2, 3, 4, 5, 6]
# op_cnt = [2, 1, 1, 1]


n = int(input())
arr = list(map(int,input().split()))
op_cnt = list(map(int,input().split()))

op = []

# op 에 대한 순열 구하기
for i in range(4):
    for j in range(op_cnt[i]):
        op.append(i)

op = list(set(permutations(op)))

# 수식 끼워넣기
def bfs(op):
    q = deque(arr)
    op = deque(op)
    while op:
        a = q.popleft()
        b = q.popleft()
        o = op.popleft()
        if o == 0:
            q.appendleft(a+b)
        elif o == 1:
            q.appendleft(a-b)
        elif o == 2:
            q.appendleft(a*b)
        elif o == 3:
            if a < 0 and b > 0:
                q.appendleft(-1*(abs(a)//b))
            else:
                q.appendleft(a//b)

    return list(q)[0]

result = []
for i in range(len(op)):
    result.append(bfs(op[i]))

print(max(result))
print(min(result))
