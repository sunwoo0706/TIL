def solution(T):
    S = [[T[0]]]
    for i in range(1, len(T)):
        t = T[i]
        s = S[i-1]
        arr = []
        arr.append([t[0] + s[0][0]])
        for j in range(1, len(t)-1):
            arr.append([t[j] + s[j-1][-1], t[j] + s[j][0]])        
        arr.append([t[-1] + s[-1][0]])
        S.append(arr)
    print(S)
    return max(sum(S[-1], []))
        

T = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(T))