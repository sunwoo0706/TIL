# https://programmers.co.kr/learn/courses/30/lessons/42627

# 각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때, 
# 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return 하도록 solution 함수를 작성해주세요. (단, 소수점 이하의 수는 버립니다)
# ***하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.

import heapq

def solution(jobs):
    answer = 0
    start = 0 # 현재까지 진행된 작업 시간
    n = len(jobs) 
    jobs.sort(key=lambda x:x[1]) # 소요시간으로 정렬

    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= start: # 현재 진행 시간보다 요청 시간이 작으면 => 작업 수행 가능
                start += jobs[i][1]
                answer += start - jobs[i][0]
                jobs.pop(i)
                break

            if i == len(jobs) - 1: # 하드디스크 놀 경우
                start += 1

    return answer // n




jobs = [[1, 3], [1, 9], [2, 6], [4, 3]]	
jobs = [[0, 3], [1, 9], [500, 6]]
print(solution(jobs))