# https://programmers.co.kr/learn/courses/30/lessons/42897

# 각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 solution 함수를 작성하세요.
# 인접한 두 집을 털면 경보가 울립니다.

def solution(money):
    
    # 0 부터 시작
    dp = money.copy()
    dp[2] += dp[0]
    for i in range(3, len(money)-1):
        dp[i] += max(dp[i-2], dp[i-3])
    m = max(dp[-3], dp[-2])
    
    # 1부터 시작
    dp = money.copy()
    dp[3] += dp[1]
    for i in range(4, len(money)):
        dp[i] += max(dp[i-2], dp[i-3])
    n = max(dp[-1], dp[-2])                                                                                                                                             
    return max(m, n)

    
money = [1, 2, 4, 9, 5, 3, 7]	
# money = [1, 2, 3, 1]
money = [3, 1, 3, 4]
print(solution(money))