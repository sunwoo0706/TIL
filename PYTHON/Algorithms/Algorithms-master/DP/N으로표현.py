# https://programmers.co.kr/learn/courses/30/lessons/42895

# 12 = 5 + 5 + (5 / 5) + (5 / 5)
# 12 = 55 / 5 + 5 / 5
# 12 = (55 + 5) / 5

# 5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
# 이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

# N은 1 이상 9 이하입니다.
# number는 1 이상 32,000 이하입니다.
# 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
# 최솟값이 8보다 크면 -1을 return 합니다.

def solution(N, number):
    if(number == N): 
        return 1
    
    d ={ 1: {N} }
    for k in range(2, 9):
        tmp = {int(str(N)*k)}
        print(tmp)
        for i in range(1, k//2+1):   
            arr = tmp
            for b in d[k-i]:
                for a in d[i]:            
                    arr = arr.union({a+b, a-b, b-a, a*b})
                    if b != 0:
                        arr.add(a//b)
                    if a != 0:
                        arr.add(b//a)
            tmp = tmp.union(arr)
            if number in tmp:
                return k
        d[k] = tmp
        print(k, d[k])
        
    return -1




n = 5
number = 12

print(solution(n, number))
