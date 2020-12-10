import math
def solution(progresses, speeds):
	answer = []

	p = [100-x for x in progresses]
	k = list(map(lambda x, y: math.ceil(x/y), p, speeds))
	answer.append(1)
	prev = k[0]

	for i in range(1, len(k)):
		if prev >= k[i]:
			answer[-1] += 1
		else:
			prev = k[i]
			answer.append(1)

	return answer

def solution2(progresses, speeds):
	prev = 0
	answer = []
	for p, k in zip(progresses, speeds):
		a = math.ceil((100-p)/k)
		if prev >= a:
			answer[-1] += 1
		else:
			prev = a
			answer.append(1)
	return answer

progresses =  [40, 93, 30, 55, 60, 65]
speeds = [60, 1, 30, 5 , 10, 7]
print(solution2(progresses, speeds))