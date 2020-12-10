def solution(N, number):
    if(number == N): 
        return 1
    
    obj ={ 1: {N} }
    for k in range(2, 9):
        tmp = {int(str(N)*k)}
        for i in range(1, k//2+1):   
            arr = tmp
            for b in obj[k-i]:
                for a in obj[i]:            
                    arr = arr.union({a+b, a-b, b-a, a*b})
                    if b != 0:
                        arr.add(a//b)
                    if a != 0:
                        arr.add(b//a)
            tmp = tmp.union(arr)
            if number in tmp:
                return k
        obj[k] = tmp
        
    return -1

N = 2
number = 11
print()
print(solution(N, number))


