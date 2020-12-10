# https://programmers.co.kr/learn/courses/30/lessons/42584

# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 

def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i] > prices[j]:
                break
            else:
                answer[i] += 1

    return answer



prices = [1, 2, 3, 2, 3]
print(solution(prices))