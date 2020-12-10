def solution (heights):
	answer = []
	stk = heights
	tmp = []
	is_cur = True
	cur = 0

	while len(stk) >= 1:
		is_cur = True
		cur = stk.pop()
		
		idx = 0
		while is_cur and len(stk) > 0:
			
			print(cur, stk[-1])
			if cur >= stk[-1]:
				tmp.append(stk.pop())
				is_cur = True
			else:
				is_cur = False

			idx = len(stk)

		while len(tmp) > 0:
			stk.append(tmp.pop())

		answer.append(idx)

	answer.reverse()
	return answer



heights = [3,9,9,3,5,7,2]
print("A", solution(heights))

