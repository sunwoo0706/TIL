import itertools 
def solution2(brown, yellow):
	res = brown + yellow
	r = make_comb(res, res//2)
	for i, k in enumerate(r):
		x = k[0]
		y = k[1]
		print(x, y)
		yellow_x = x - 2
		yellow_y = y - 2
		if yellow_x * yellow_y == yellow:
			return[x, y]

	return []

def make_comb(res, n):
	r = []
	for i in range(1, n):
		if res % i == 0:
			k = res // i
			if k >= i:
				r.append((k, i))

	return r


def solution(brown, red):
	for i in range(1, int(red**(1/2))+1):
		if red % i == 0:
			print(i, red)
			if 2*(i + red//i) == brown-4:
				return [red//i+2, i+2]



# print(solution(10, 2))
print(solution(24, 24))
# print(solution(8, 1))