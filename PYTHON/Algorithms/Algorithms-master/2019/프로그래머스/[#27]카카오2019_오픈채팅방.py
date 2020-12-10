def solution(record):

	nick = dict()
	s = []
	# 닉네임 저장
	for r in record:
		x = r.split()
		if x[0] != "Leave":
			nick[x[1]] = x[2]
		s += [(x[0], x[1])]

	res = []
	for command, user_id in s:
		if command == "Leave":
			c = "나갔습니다."
		elif command == "Enter":
			c = "들어왔습니다."
		else:
			continue
		res += [nick[user_id] + "님이 " + c]



	return res



print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))