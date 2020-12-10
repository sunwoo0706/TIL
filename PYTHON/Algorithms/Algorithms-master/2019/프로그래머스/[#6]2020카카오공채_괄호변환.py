def solution(p):
	answer = create(p)
	return answer

def create(w):
	if w == '':
		return ''

	u, v = split_parenthesis(w)

	if is_correct(u):
		if v == '':
			return u
		else: 
			v = create(v)
		u += v
		return u

	else:
		answer = ''
		answer += '('
		v = create(v)
		answer += v
		answer += ')'

		u = u[1:-1]
		u = u.replace('(','0').replace(')','(').replace('0',')')
		
		answer += u

		return answer


def split_parenthesis(w):
	u = ''
	v = ''
	c_right = 0
	c_left = 0
	for i in range(len(w)):
		if(c_right == c_left and c_right > 0 and c_left > 0):
			break
		u += w[i]
		v = w[i+1:]
		if(w[i] == '('):
			c_right += 1
		else:
			c_left += 1
	
	return u, v


def is_correct(u): 
	stk = ['top'] # stack
	stk.append(u[0])

	for i in range(1, len(u)):
		if u[i] == ')' and stk[-1] == '(':
			stk.pop()
		else:
			stk.append(u[i])

	if len(stk) == 1:
		return True

	return False


