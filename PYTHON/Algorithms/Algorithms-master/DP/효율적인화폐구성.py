
m = 15

n = 2
arr = [2, 3]

# m = 4
# n = 3
# arr = [2, 5, 7]

d = [10001] * 10000



d[0] = 0
arr.sort()
for i in arr:
    d[i] = 1

for j in range(n):
    for i in range(arr[j], m+1):    
        if d[i-arr[j]] != 10001:
            d[i] = min(d[i], d[i-arr[j]] + 1)
    
if d[m] == 10001:
    print(-1)
else:
    print(d[m])


