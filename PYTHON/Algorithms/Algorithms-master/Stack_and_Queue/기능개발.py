# https://programmers.co.kr/learn/courses/30/lessons/42586

import math

def solution(progresses, speeds):
    d = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))] # 수행 날짜
    stack = [d[0]]
    answer = [1]
    for i in range(1, len(d)):
        if stack[-1] < d[i]:
            stack.append(d[i])
            answer.append(1)
        else:
            answer[-1] += 1
        print(stack)
    return answer

progresses = [93, 30, 55] # 진도
speeds = [1, 30, 5]	# 작업속도

progresses = [95, 90, 99, 99, 80, 99]	
speeds = [1, 1, 1, 1, 1, 1]	

print(solution(progresses, speeds))