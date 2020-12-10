# https://programmers.co.kr/learn/courses/30/lessons/43163

# 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.
# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.

# 두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

from collections import deque

def solution(begin, target, words):
    # 모든 경우에서 bfs 돌리기
    visited = [0 for _ in range(len(words))]
    q = deque([(begin, 0)])

    while q:
        p = q.popleft()
        s = p[0]
        cnt = p[1]
        if s == target:
            return cnt
        for i in range(len(words)):
            # d = diff(words[i], s) # 단어 2개간 개수 차이 구하기

            d = sum([x!=y for x, y in zip(words[i], s)]) # 단어 2개간 개수 차이 구하기

            if visited[i] == 0 and d == 1:
                visited[i] = 1
                q.append((words[i], cnt+1))
    return 0


def diff(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    return cnt


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
# words = ["hot", "dot", "dog", "lot", "log"]
print(solution(begin, target, words))