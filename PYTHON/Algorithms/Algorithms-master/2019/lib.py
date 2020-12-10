def lam():
	# 소수 구하기
	is_prime = lambda x: x > 1 and all([x % i for i in range(2, int(math.sqrt(x) + 1))])

# 최대공약수
def gcd(a,b): 
	return b if (a==0) else gcd(b%a,a)    
