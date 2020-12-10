# https://programmers.co.kr/learn/courses/30/lessons/49190

# 사방이 막히면 방하나로 샙니다.
# 이동하는 방향이 담긴 배열 arrows가 매개변수로 주어질 때, 
# 방의 갯수를 return 하도록 solution 함수를 작성하세요.

from collections import defaultdict
def solution(arrows):
    dx = [0,1,1,1,0,-1,-1,-1]
    dy = [1,1,0,-1,-1,-1,0,1]
    
    
    now = start = (0, 0)
    visited = set([start])
    edges = defaultdict(int)
    answer = 0

    for i in arrows:
        for _ in range(2):
            nx, ny = (now[0]+dx[i], now[1]+dy[i])
            if (nx, ny) in visited and edges[(now[0], now[1], nx, ny)] == 0:
                answer += 1
            edges[(nx, ny, now[0], now[1])] += 1
            edges[(now[0], now[1], nx, ny)] += 1
            visited.add((nx, ny))
            now = (nx, ny)
    
    return answer




    
arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]	
arrows = [6, 5, 2, 7, 1, 4, 2, 4, 6]
arrows = [5, 2, 7, 1, 6, 3]
# arrows = [6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0]
print(solution(arrows))