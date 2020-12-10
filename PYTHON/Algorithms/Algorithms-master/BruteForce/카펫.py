# https://programmers.co.kr/learn/courses/30/parts/12230

# 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다. (가로>=세로)
# 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 

# 먼저 yellow를 2개의 곱으로 분해하기!
# 그다음 각각을 탐색해서 brown 개수랑 일치하는지!
# ex) yellow=24=4x6 => brown = (4 + 6) * 2 + 모서리개수(=4)

def solution(brown, yellow):
    case = []

    for y in range(1, yellow//2 + 1):
        x = yellow // y
        if yellow % y == 0 and x >= y:
            case.append((x, y))
    
    if yellow == 1:
        case.append((1, 1))

    for x, y in case:
        predict = (x + y)*2 + 4
        if predict == brown:
            return [x+2, y+2]

    return 0
    

brown = 10
yellow = 2

# brown = 8
# yellow = 1

brown = 24
yellow = 24
print(solution(brown, yellow))