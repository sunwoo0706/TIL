# https://programmers.co.kr/learn/courses/30/lessons/60058
# 2020 카카오 신입 공채 1차

def solution(p):
    w = list(p)
    if w == []:
        return ""
    
    u, v = split_valnced(w)
    
    
    if is_correct(u):
        r = list(solution(v))
        u += r
        return ''.join(u)
    else:
        s = ['(']
        r = solution(v)
        s += list(r)
        s.append(')')
        u = u[1:-1]
        u = list(map(lambda x: ')' if x == '(' else '(', u))
        s += u

        return ''.join(s)


# 올바른 문자열인지 판단 = stack으로
def is_correct(u):
    stack = [u[0]]
    for i in range(1, len(u)):
        if u[i] == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(u[i])
    
    if len(stack) == 0:
        return True
    return False



# u, v로 나누기
def split_valnced(w):
    # u: 균형잡힌 문자열로 더이상 분리할 수 없다. (빈 문자열 안됨)
    # v: 더 분리 가능, 빈 문자열도 가능
    p = 0
    q = 0
    cnt = 0
    u = []
    for i in w:
        cnt += 1

        if i == '(':
            p += 1
        else:
            q += 1

        u.append(i)

        if p == q and p != 0 and q != 0:
            break

    return u, w[cnt:]


p = "(()())()"
#p = "()))((()"
#p = ")(()()"
#p = ")("

print(solution(p))