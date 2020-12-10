# facebook interview

s = '3012345'
arr = list(map(int, list(s)))

answer = arr[0]
for i in range(1, len(arr)):
	if arr[i-1] <= 1 or arr[i] <= 0:
		answer += arr[i]
	else:
		answer *= arr[i]
		
print(answer)