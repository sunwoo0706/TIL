def solution(N):
    obj = [(1,1)]
    
    for i in range(1, N):
        if i % 2 == 0:
            obj.append((obj[i-1][0] + obj[i-1][1], obj[i-1][1]))
        else:
            obj.append((obj[i-1][0], obj[i-1][1] + obj[i-1][0]))
        
    return (obj[N-1][0]+obj[N-1][1])*2