n = 3
m = 3
arr = [[3, 1, 2], [4, 1, 4], [2, 2, 2]]

result = 0
for i in range(n):
	min_value = min(arr[i])
	if result < min_value:
		result = min_value

print(result)