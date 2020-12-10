# https://programmers.co.kr/learn/courses/30/lessons/60061
# 카카오 2020 신입공채
# 구현


def possible(answer):
    # answer.sort(key=lambda x:(x[0], x[1]))
    for x, y, a in answer:
        if a == 0:  # 기둥
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False

        elif a == 1: # 보
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False

    return True


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 1: # 설치
            answer.append([x, y, a])
            if not possible(answer):
                answer.remove([x, y, a])
                
        else: # 삭제
            answer.remove([x, y, a])
            if not possible(answer):
                answer.append([x, y, a])
    
    return sorted(answer)




n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]	
# build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))