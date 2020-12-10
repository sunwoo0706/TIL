# https://programmers.co.kr/learn/courses/30/lessons/43164



def solution(tickets):
    tickets.sort(key=lambda x: x[1])
    result = []
    start = "ICN" # 처음 start는 ICN
    result.append(start)
    answer = dfs(start, tickets, result)

    return answer

def dfs(start, tickets, result):
    if len(tickets) == 0: # tickets이 모두 pop되면 result 리턴
        return result
    
    print(result)
    for i, ticket in enumerate(tickets): # 티켓수만큼 for문
        if start == ticket[0]: # 만약 start가 같으면
            end = ticket[1] # end를 ticket[1]
            tickets.pop(i) # tickets에서 현재 인덱스 pop
            result.append(end) # result에 end append
            tmp = dfs(end, tickets, result) # 재귀, 즉, 현재 start, end에서 end를 start로 바꿔줌
            if len(tmp) != 0: 
                return tmp # dfs 재귀한게 빈 값이 아니면 (결과가 있으면) 성공하면 리턴
            result.pop(len(result)-1) # dfs 재귀한결과 빈값이면 (결과가 없으면) result에서 마지막 애를 pop 해주고
            tickets.insert(i, [start, end]) # tickets에서 pop했던걸 다시 원래 위치에다가 insert해줌
    return []



tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	
# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "A"], ['A', 'C'], ['A', 'D'], ['D', 'B'], ['B', 'A']]	
# tickets = [['ICN' ,'B'], ['ICN', 'C'] ,['C', 'D'], ['D', 'ICN']]
# tickets = [["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]
# tickets = [["ICN", 'A'], ['A', 'C'], ['A', 'D'], ['D', 'B'], ['B', 'A']]
# tickets =[['ICN','A'],['ICN','A'],['A','ICN']]
# tickets = [['ICN', 'AAA'], ['ICN', 'BBB'], ['BBB', 'ICN']]
# tickets = [["ICN", 'A'], ['A', 'B'], ['A', 'C'], ['C', 'A'], ['B', 'D']]
print(solution(tickets))