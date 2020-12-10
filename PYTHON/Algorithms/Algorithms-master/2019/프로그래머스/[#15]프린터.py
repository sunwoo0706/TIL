def solution(priorities, location):
	answer = 0

	i = 0
	idx = [i for i in range(len(priorities))]
	res = []
	while priorities:
		m = max(priorities)
		p = priorities.pop(0)
		i = idx.pop(0)
		if p < m:
			priorities.append(p)
			idx.append(i)
		else:
			res.append(i)
	return res.index(location) + 1


print(solution([2, 1, 3, 2], 2))