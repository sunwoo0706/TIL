def solution(key, lock):
	answer = True
	print(key)

	for k in range(len(lock)**2):
		j = k % len(lock)
		i =  k // len(key)

		# print(i, j)

	keys = key_case(key)
	return answer

def key_case(key):
	arr = []
	for i in range(len(key)):
		tmp = []
		for j in range(len(key[0])):
			print(i, j)
			tmp.append(key[i][j])
		arr.append(tmp)
	print(arr)
		

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))