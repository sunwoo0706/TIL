def solution2(skill, skill_trees):
	cnt = 0
	s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in skill:
		s = s.replace(i, '')

	arr = []
	for t in skill_trees:
		for i in s:
			t = t.replace(i, '')
		arr.append(list(t))

	for i in range(len(arr)):
		chk = 1
		for j in range(len(arr[i])):
			if skill[j] != arr[i][j]:
				chk = 0
		if chk:
			cnt += 1

	return cnt



def solution(skill, skill_trees):
	answer = 0

	for skills in skill_trees:
		skill_list = list(skill)

		for s in skills:
			print(s, skill)
			if s in skill:
				if s != skill_list.pop(0):
					print('break')
					break
		else:
			print('non')
			answer += 1
		print()

	return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))