# https://programmers.co.kr/learn/courses/30/lessons/67257
# 카카오 2020 인턴

# 완전탐색

from itertools import permutations

def solution(expression):
    op = [x for x in expression if x in {'*', '-', '+'}]
    num = expression.replace('-', ',').replace('*', ',').replace('+', ',').split(',')
    
    p = list(permutations(set(op)))
    answer = 0
    for i in p:
        answer = max(answer, execute(op.copy(), num.copy(), i))
    return answer

def execute(op, num, p):

    for i in range(len(set(op))):
        while p[i] in op:
            idx = op.index(p[i])
            
            value = eval(str(num[idx]+op[idx]+num[idx+1]))
            num[idx] = str(value)
            num.pop(idx+1)
            op.pop(idx)
    return abs(int(num[0]))

    

expression = "100-200*300-500+20"	

print(solution(expression))