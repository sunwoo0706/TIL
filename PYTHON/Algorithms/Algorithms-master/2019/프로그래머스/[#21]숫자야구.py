# def solution(baseball):
# 	print(baseball)

# 	numbers = [list(str(x[0])) for x in baseball]
# 	strike = []
# 	ball = []
# 	for i, n in enumerate(numbers):
# 		print(i, n)
# 		s = baseball[i][1]
# 		b = baseball[i][2]
# 		if s >= 1:
# 			strike += set([(0, n[0]), (1, n[1]), (2, n[2])])
# 		if b >= 1 and s == 0:
# 			print(b, n[0], n[1], n[2])
# 			strike = set(strike) - set([(0, n[0]), (1, n[1]), (2, n[2])])
# 			strike += set([])

# 			# ball += [(0, n[0]), (1, n[1]), (2, n[2])]

# 		if b >= 1 and s >= 1:
# 			ball += set([(0, n[0]), (1, n[1]), (2, n[2])])
	

# 	strike = set(strike)
# 	ball = set(ball)
# 	# strike -= ball
	

# 	print(strike)
# 	print(ball)
# 	return 0


# def solution(baseball):
# 	d = {0:set(),1:set(),2:set()} # 가능한 숫자 집합

# 	for i, k in enumerate(baseball):
# 		n = list(str(k[0]))
# 		s = k[1]
# 		b = k[2]
# 		# print(n, s, b)
# 		if s == 0 and b == 0:
# 			print(k)
# 			d[0] -= {n[0]}
# 			d[1] -= {n[1]}
# 			d[2] -= {n[2]}
# 		if s >= 1 and b == 0:
# 			# print(k)
# 			d[0].add(n[0])
# 			d[1].add(n[1])
# 			d[2].add(n[2])
# 		if s == 0 and b >= 1:
# 			# print(k)
# 			d[0] -= {n[0]}
# 			d[1] -= {n[1]}
# 			d[2] -= {n[2]}
# 		if s >= 1 and b >= 1:
# 			print(k)
# 	print(d)
# 	return 0

# import itertools
# def solution(baseball):
# 	first = list(itertools.permutations(range(1, 10), 3))
# 	print(first)


def solution(baseball):
	# 가능한 숫자의 집합(순서 상관 없이)
	# 절대 안들어가는 숫자의 집합

	poss = [0 for i in range(0, 10)]
	for i, k in enumerate(baseball):
		n = list(str(k[0]))
		s = k[1]
		b = k[2]
		s_b = s + b
		print(s_b)
		print(n)





# 324, 328 : 2가지
print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))