from functools import reduce
import collections

def solution(clothes):
	d = {}

	for c, t in clothes:
		if t not in d:
			d[t] = 2
		else:
			d[t] += 1

	cnt = 1
	print(d)
	for num in d.values():
		cnt *= num 

	return cnt - 1

def solution2(clothes):
	d = collections.Counter(x[1] for x in clothes)
	print(d)
	answer = reduce(lambda x, y: x*y, [x+1 for x in d.values()]) - 1
	return answer



clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"], ["a", "a"], ["b", "b"]]
# clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution2(clothes))
