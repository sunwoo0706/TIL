# https://programmers.co.kr/learn/courses/30/lessons/60059
# 카카오 2020 신입공채

import copy
def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0]*(n*3) for _ in range(n*3)]

    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    # 4 방향으로 rotate
    for _ in range(4):
        key = rotate(key)
        for x in range(n*2):
            for y in range(n*2):

                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                
                if check(new_lock) == True:
                    return True
                
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]  
    return False

def check(new_lock):
    n = len(new_lock) // 3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if new_lock[i][j] != 1:
                return False
    return True 

def rotate(key):
    new_key = copy.deepcopy(key)
    n = len(key)
    for i in range(n):
        for j in range(n):
            new_key[i][(n-1)-j] = key[j][i]
    return new_key
    

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
