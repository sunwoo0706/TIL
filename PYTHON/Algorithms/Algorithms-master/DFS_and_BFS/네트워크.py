# https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque

# def solution(n, computers):
#     c = [[] for _ in range(n)]
#     v = [False]*n # 방문노드 체크

#     for i in range(n):
#         for j in range(n):
#             if computers[i][j] == 1 and i != j:
#                 c[i].append(j)
#     # print(c)
#     queue = deque([0])
#     v[0] = True
#     answer = 0
#     while queue:
#         answer += 1
#         print('a', answer, v, c, queue)
#         q = queue.popleft()
#         for i in c[q]:
#             print('test', i)  
#             if not v[i]:
#                 print('i;', i)
#                 queue.append(i)
#                 v[i] = True
#         print()
#     return answer
            
def solution(n, computers):
    c = [[] for _ in range(n)]
    visited = [False]*n # 방문노드 체크

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                c[i].append(j)
    print(c)
    answer = 0

    for i in range(n):
        if dfs(c, i, visited) == True:
            answer += 1

    return answer     

def dfs(graph, v, visited):
    if visited[v] == True:
        return False

    visited[v] = True
    # print('v: ', v, end=' ')
    
    
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)
    return True



n = 3 # 컴퓨터 개수
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]] # computers[i][j] = 1 : 컴퓨터 i, j 가 연결되어있음
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
computers = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print(solution(n, computers))


<a href="https://elasticbeanstalk-us-west-2-800068098556.s3.amazonaws.com/challenge-website/public_data_with_labels/test.tsv?AWSAccessKeyId=AKIA3UR6GLH6F73MJVWF&amp;Signature=9lxuOiyCZBG38FpxTL7VHy59UXo%3D&amp;Expires=1604548207"> click to download </a>