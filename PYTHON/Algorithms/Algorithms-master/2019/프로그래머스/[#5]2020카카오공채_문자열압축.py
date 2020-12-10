def solution(s):
	answer = len(s)
	step = 1
	current = ""
	num = 1
	for length in range(1, (len(s)+1)): # step size
		current = ""
		cut = [s[i:i+length] for i in range(0, len(s), length)]
		for i in range(len(cut)):
			prev = current
			current = cut[i]
			if(prev == current): 
				num += 1
				cut[i-(num-1)] = str(num)
				if(num > 2):
					cut[i] = ""
			else:
				num = 1

		res = "".join(cut)

		if(answer > len(res)):
			answer = len(res)

	return answer



# s = "abcabcdede"
# s = "aabbaccc"
# s = "ababcdcdababcdcd"
# s = "abcabcabcabcdededededede"
s = "xababcdcdababcdcd"
print(solution(s))