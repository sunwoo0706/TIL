n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

start = 0
end = a[-1]

result = 0

while start <= end:
    mid = (start + end) // 2
    
    total = 0
    for x in a:
        if x > mid:
            total += x - mid 
    
    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1 

print(result)