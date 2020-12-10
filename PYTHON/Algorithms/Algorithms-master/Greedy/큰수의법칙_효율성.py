n = 5
m = 8
k = 3

data = [3, 1, 2, 5, 3]

data.sort()

first = data[-1]
second = data[-2]

count = int(m//(k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)