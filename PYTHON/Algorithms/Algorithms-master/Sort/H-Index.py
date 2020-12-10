# https://programmers.co.kr/learn/courses/30/lessons/42747


# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

def solution(citations):
    
    citations.sort(reverse=True)
    answer = 0
    h = 1
    for i in range(len(citations)):
        citations = list(map(lambda x: x-1 if x > 0 else x , citations))
        n = len(list(filter(lambda x: x > 0, citations)))
        h += 1
        if n >= h and len(citations) - n <= h:
            answer = h

    return answer



citations = [3, 0, 6, 1, 5, 0, 9]	
print(solution(citations))