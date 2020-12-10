# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for c in commands:
        i = c[0]-1
        j = c[1]-1
        k = c[2]-1
        
        arr = sorted(array[i:j+1])
        answer.append(arr[k])
    return answer




array = [1, 5, 2, 6, 3, 7, 4]	
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	
print(solution(array, commands))