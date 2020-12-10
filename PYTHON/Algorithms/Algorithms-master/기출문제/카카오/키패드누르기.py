# https://programmers.co.kr/learn/courses/30/lessons/67256
# 카카오 2020 인턴

def solution(numbers, hand):
    d = dict({
        2: [1, 0, 1, 2, 1, 2, 3, 2, 3, 4, 3, 4], 
        5: [2, 1, 2, 1, 0, 1, 2, 1, 2, 3, 2, 3], 
        8: [3, 2, 3, 2, 1, 2, 1, 0, 1, 2, 1, 2], 
        11: [4, 3, 4, 3, 2, 3, 2, 1, 2, 1, 0, 1]
        })
    l = 10
    r = 12
    answer = []

    for n in numbers:       
        if n in {1, 4, 7}:
            l = n
            answer.append('L')
        elif n in {3, 6, 9}:
            r = n
            answer.append('R')
        else:
            if n == 0:
                n = 11
            distance = d[n]
            d_l = distance[l-1]
            d_r = distance[r-1] 
            
            if d_l == d_r:
                if hand == 'right':
                    r = n
                    answer.append('R')                    
                else:
                    l = n
                    answer.append('L')
            elif d_l > d_r:
                r = n
                answer.append('R')
            else:
                l = n
                answer.append('L') 
    
    return ''.join(answer)

    
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	
hand = "right"

print(solution(numbers, hand))