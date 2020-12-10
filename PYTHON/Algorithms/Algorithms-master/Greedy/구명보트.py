# https://programmers.co.kr/learn/courses/30/lessons/42885

#  구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.
# 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

def solution(people, limit):
    people.sort()
    answer = 0
    l, r = len(people)-1, 0 # 정렬된 애들을 왼쪽방향, 오른쪽방향으로 가게한다!

    while r <= l:
        if people[r] + people[l] <= limit:
            r += 1
        l -= 1
        answer += 1g
        
    return answer

people = [70, 50, 80, 50]
limit = 100

people = [70, 80, 50]	
print(solution(people, limit))