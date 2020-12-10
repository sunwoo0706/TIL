def solution2(citations):
    citations.sort(reverse=True)
    for i, j in enumerate(citations):
    	print(i)
    print(citations)
    print(list(map(min, enumerate(citations, start=1))))
    answer = max(map(min, enumerate(citations, start=1)))
    return answer



def solution(citations):
	citations = sorted(citations)
	l = len(citations)
	for i in range(l):
		print(citations[i], l-i)
		if citations[i] >= l-i:

			return l-i
	return 0

print(solution([3, 0, 6, 1, 5]))