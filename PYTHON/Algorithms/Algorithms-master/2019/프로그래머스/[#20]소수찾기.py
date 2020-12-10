import math
import itertools
def solution(numbers):
	n = list(numbers)
	is_prime = lambda x: x > 1 and all([x % i for i in range(2, int(math.sqrt(x) + 1))])
	cnt = 0
	p = []
	for i in range(1, len(numbers)+1):
		p += list(map(list, itertools.permutations(numbers, i)))
	p = set([int(''.join(x)) for x in p])
	for i in p:
		if is_prime(int(i)):
			print(i)
			cnt += 1
	print(set(range(0, 2)))
	return cnt

def solution2(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)




# print(solution("17")) # 1, 7, 17, 71
print(solution("011")) # 1, 5, 7, 15, 17, 51, 7, 1, 71  