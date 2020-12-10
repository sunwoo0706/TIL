# https://programmers.co.kr/learn/courses/30/lessons/42860

# 만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return
def solution(name):
    pattern = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    res = list("A"*len(name))
    name = list(name)
    v = [0]*len(name)
    visited = 0
    p = 0 # 좌우 커서키 
    q = 0 # 상하 알파벳 이동 

    # 알파벳 변경
    while visited < len(name):
        visited += 1

        q = 0
        q_flag = -1
        a = pattern.index(res[p])
        b = pattern.index(name[p])
        if b-a < len(pattern) + a -b:
            q_flag = 1
                
        while res[p] != name[p]:
            q += q_flag
            res[p] = pattern[q]
            v[p] += 1

        p += 1

    # 좌우 커서키 그리디로 이동
    left, right = -1, 1
    res = list("A"*len(name))
    p = 0
    answer = v[p]
    res[p] = name[p]
    while name != res:
        while v[p+left] == 0:
            left -= 1

        while v[p+right] == 0:
            right += 1
    
        if abs(left) < right:
            p += left
            answer += abs(left)
            left = -1
        else:
            p += right
            answer += right
            right = 1

        if name[p] != res[p]:
            answer += v[p]
        v[p] = 0
        res[p] = name[p]

    return answer


name = "JEROEN" # 56
name = "JAN" # 23
name = "JAZ" # 11
# name = "BBBBAAAABA" # 12
name = "ABAAAAAAABA" # 6
name = "AZAAAZ"
# name = "AZAAAAAAAZZ"
# name = "BABAAAAB"
print(solution(name))