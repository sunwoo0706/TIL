def solution(arr):
	answer = 0
	cnt = 0
	
	arr = list(arr)
	prev = ""

	while arr:
		p = arr.pop(-1)
		
		if prev == ")" and p == ")":
			cnt += 1
			answer += 1

		if prev == "(" and p == "(":
			cnt -= 1

		if prev == ")" and p == "(":
			answer += cnt
		prev = p
	
	return answer

# print(solution("(())((()))"))
print(solution("()(((()())(())()))(())"))