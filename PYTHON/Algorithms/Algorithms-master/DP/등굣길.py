# https://programmers.co.kr/learn/courses/30/lessons/42898

# 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다
# 격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다. 
# 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.


# dfs 돌리고 dp 테이블에 값 누적해서 저장하기~!

from collections import deque
def solution(m, n, puddles):
    dp = [[1 for _ in range(m)] for _ in range(n)]

    dx = [1, 0]
    dy = [0, 1]
    for x, y in puddles:
        dp[y-1][x-1] = 0

        if x-1 == 0:
            for k in range(y-1,n):
                dp[k][0] = 0
        if y-1 == 0:
            for k in range(x-1,m):
                dp[0][k] = 0
   
    for x in range(n):
        for y in range(m):
            if x * y != 0:
                if dp[x][y] != 0:
                    dp[x][y] = dp[x-1][y] + dp[x][y-1]
    
   
    return dp[n-1][m-1]%1000000007


m = 4
n = 3
puddles = [[2, 2]]	
puddles = [[1, 3]]	
print(solution(m, n, puddles))