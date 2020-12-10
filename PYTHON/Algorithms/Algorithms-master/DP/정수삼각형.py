# https://programmers.co.kr/learn/courses/30/lessons/43105

# 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 
# 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 
# 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

def solution(triangle):
    d = triangle.copy()

    for i in range(1, len(triangle)):
        for j in range(0, i+1):
            if j == 0:
                d[i][j] += d[i-1][0]
            elif j == i:
                d[i][j] += d[i-1][j-1]
            else:
                d[i][j] += max(d[i-1][j-1], d[i-1][j])

    return max(d[-1])

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	

print(solution(triangle))