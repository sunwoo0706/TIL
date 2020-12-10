# https://programmers.co.kr/learn/courses/30/lessons/42587

# 중요도가 높은 문서를 먼저 인쇄하는 프린터 => 우선순위 큐
# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.

# 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location (0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하)
# 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return


from collections import deque


def solution(priorities, location):
    q = deque([(p, i) for i, p in enumerate(priorities)])

    t = 0
    while len(q) >= 1:
        p = q.popleft()
        m = sum([p[0] < x[0] for x in q])
        if m:
            q.append(p)
        else:
            t += 1
            if p[1] == location:
                break

        
    return t


priorities = [2, 1, 3, 2]
location = 2

priorities = [1, 1, 9, 1, 1, 1]	
location = 0

print(solution(priorities, location))





from queue import PriorityQueue

def solution2(priorities, location):
    q = PriorityQueue()
    # q.put(1)
    for i, p in enumerate(priorities):
        q.put((-p, i))

    t = 0
    while q:
        t += 1
        p = q.get()
        print(p)
        if p[1] == location:
            break

    return t