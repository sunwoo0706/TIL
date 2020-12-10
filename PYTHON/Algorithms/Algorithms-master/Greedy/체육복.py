# https://programmers.co.kr/learn/courses/30/lessons/42862

# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

def solution(n, lost, reserve):
    _lost = set(lost) - set(reserve)
    _reserve = set(reserve) - set(lost)
    
    save = n - len(_lost)

    for x in _reserve:
        if x-1 in _lost:
            save += 1
            _lost.remove(x-1)
        elif x+1 in _lost:
            save += 1
            _lost.remove(x+1)
        
    return save

n = 5
lost = [2, 4]
reserve = [3]
print(solution(n, lost, reserve))
