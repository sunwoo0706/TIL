
n = 26

d = [0] * 30001

for i in range(2, n+1):
    d[i] = d[i-1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)

        
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)


print(d[n])
    






################

k = 1
t = 0
while True:
    
    if k == n:
        break
    if k * 5 <= n:
        k *= 5
    
    elif k * 3 <= n:
        k *= 3

    elif k * 2 <= n:
        k *= 2
    
    else:
        k += 1

    t += 1

print(t)