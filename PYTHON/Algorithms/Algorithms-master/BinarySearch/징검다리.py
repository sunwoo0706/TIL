# https://programmers.co.kr/learn/courses/30/lessons/43236
# 다시 풀어보기

# 바위를 n개 제거해서 얻을 수 있는 바위사이의 최소값 중에 가장 큰 값
def solution(distance, rocks, n):
    rocks.sort()
    start = 1
    end = distance

    answer = 0

    # 무엇을 뺄 것인가?
    # 기준에 맞춰서 빼주고, 빼준 돌 갯수가 만족하는지 여부로 결정
    # 빠진 돌개수를 세어주기
    while start <= end:
        mid = (start + end) // 2
        pre_rock = 0 # 이전에 선택된 rock (거리 구하기 위해서)
        cnt = 0 # 제거한 바위 개수
        min_value = 1000000001 # 최소값 초기화
        for rock in rocks:
            if rock - pre_rock < mid: # 현재 rock이랑 이전 rock뺀게 mid 보다 작으면 == 최소값을 안만드므로 해당 바위를 제거함
                cnt += 1 # 제거한 바위 개수 1 증가
            else: # 현재 rock이랑 이전 rock 뺀게 mid 보다 크거나 같으면 == 최소값을 바꿔줘야함
                min_value = min(min_value, rock - pre_rock) # 최소값을 바꿔주기
                pre_rock = rock # 이전 rock을 바꿔주기
        
        if cnt > n: # 제거한 바위가 더크면 == 더 많이 제거해아한다는것! 따라서 최대값이 줄어든다
            end = mid - 1
        else: # 작거나 같으면 => 덜 제거해도 된다는 것. 최대값이 늘어난다.
            answer = min_value # 답을 최소값으로 바꿔줌
            start = mid + 1

    return answer



distance = 25
rocks = [2, 14, 11, 21, 17]	
n = 2

print(solution(distance, rocks, n))
