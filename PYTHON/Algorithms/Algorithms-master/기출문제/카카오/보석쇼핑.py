# https://programmers.co.kr/learn/courses/30/lessons/67258
# 카카오 2020 인턴
# 매장 진열대의 특정 범위의 물건들을 모두 싹쓸이 구매하는 습관
# 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매

# 풀이) 해쉬, 투포인터 알고리즘

def solution(gems):
    n = len(set(gems))
    start, end = 0, 0 # 둘다 0부터 시작
    answer = [0, len(gems) - 1]
    visited = dict({gems[0]:1})

    while start < len(gems) and end < len(gems):
        if len(visited) == n: # 모든 아이템 방문하면
            if answer[1] - answer[0] > end - start: # 더 앞에 있는거로 answer 바꿔줌
                answer[0] = start
                answer[1] = end
            if visited[gems[start]] == 1: # gems[start] 하나 삭제하고 start 포인트 앞으로 이동 시키기
                del visited[gems[start]]
            else:
                visited[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == len(gems): # end가 끝이면 break
                break
            else:
                if visited.get(gems[end]) is None: # gems[end] 하나 증가시킴 (end 뒤로 이동시켰으니까)
                    visited[gems[end]] = 1  
                else:
                    visited[gems[end]] += 1
    
    return [answer[0]+1, answer[1]+1]

# gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA","RUBY", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	
# gems = [ "AB", "K", "AB", "K", "AA" ,"AC", "AB"]
gems = ["XYZ", "XYZ", "XYZ"]	
print(solution(gems))