# number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자
# https://programmers.co.kr/learn/courses/30/lessons/42883


def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


number = "1924"
k = 2

# number = "1231234"
# k = 3

number= "99991"
k = 2
print(solution(number, k))