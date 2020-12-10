n = 3
d = [0]*1000 # 해당 iteration에서 모든 경우의 수를 dp테이블에 담는다.

d[1] = 1
d[2] = 3

for i in range(3, n+1):

    d[i] = (d[i-1] + d[i-2]*2)%7967966

print(d[n])
