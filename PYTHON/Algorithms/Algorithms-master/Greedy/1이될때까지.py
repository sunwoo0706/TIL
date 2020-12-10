n, k = map(int, input().split())
result = 0
i = 0
while True:
	target = (n // k) * k
	result += (n - target)
	n = target
	
	if n < k:
		break

	result += 1
	n //= k

print(result-1)

