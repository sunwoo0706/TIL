def solution(answers):
	a = [1, 2, 3, 4, 5]
	b = [2, 1, 2, 3, 2, 4, 2, 5]
	c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
	k = [0 for i in range(3)]
	for i in range(len(answers)):
		a_idx = i - len(a) * (i // len(a))
		b_idx = i - len(b) * (i // len(b))
		c_idx = i - len(c) * (i // len(c))
		if answers[i] == a[a_idx]:
			k[0] += 1
		if answers[i] == b[b_idx]:
			k[1] += 1
		if answers[i] == c[c_idx]:
			k[2] += 1
	m = max(k)
	k = list(map(lambda x: (x[0], x[1]), enumerate(k, start=1)))
	k.sort(key = lambda x : x[1], reverse=True)

	a = []
	for i, j in k:
		if j == m:
			a.append(i)
			
	return a


print(solution([1,3,2,4,2]))
print(solution([1,2,3,4,5]))