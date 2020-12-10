# https://programmers.co.kr/learn/courses/30/lessons/42746


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=lambda x:x*3)

    return str(int(''.join(numbers)))
    
    # 333 343434 303030 문자열 비교

numbers = [6, 10, 2]
numbers = [3, 30, 34, 5, 9]	
print(solution(numbers))