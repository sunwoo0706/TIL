# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def solution(numbers):
    n = []
    for i in range(len(numbers)):
        n += set(map(lambda x: int(''.join(x)),permutations(numbers, i+1)))
    
    n = set(n)
    return sum(list(map(lambda x: isPrime(x), n)))
    
def isPrime(n):
    if n < 2:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return 0 
    return 1


    

numbers = "17"
numbers = "011"
print(solution(numbers))