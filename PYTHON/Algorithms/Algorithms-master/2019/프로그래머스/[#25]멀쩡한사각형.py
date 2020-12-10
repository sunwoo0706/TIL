import fractions

def solution(w, h):
	# w와 h의 최대공약수가 1인 경우: (w * h) - (w + h - 1) = 정사각형 갯수
	# w와 h의 최대공약수가 2이상인 경우: (w * h) - (w + h - 최대공약수) = 정사각형 갯수
	f = fractions.Fraction(min(w, h), max(w, h))
	a = f.numerator #분자
	b = f.denominator #분모
	k = max(w, h) // b # 최대공약수
	print(k)
	return ((w * h) - (w + h - k))

def gcd(a,b): return b if (a==0) else gcd(b%a,a)    

print(solution(4, 8))
print("--------")
print(solution(12, 8))
print("--------")
print(solution(3, 7))
print("--------")
print(solution(2, 4))
