n = 5
m = 8
k = 3

data = [3, 1, 2, 5, 3]

data.sort()

first = data[-1]
second = data[-2]

result = 0

while True:
	for i in range(k):
		if m == 0:
			break
		result += first
		m -= 1
	if m == 0:
		break
	result += second
	m -= 1



print(result)