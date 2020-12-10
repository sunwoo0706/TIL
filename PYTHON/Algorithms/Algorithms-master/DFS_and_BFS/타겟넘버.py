def solution(numbers, target):

    if len(numbers) == 1:
        if numbers[0] == target or numbers[0] == -target:
            return 1
        else:
            return 0
    
    a = numbers.pop()
    b = numbers.pop()

    # + 인경우 dfs 돌리기
    res1 = solution(numbers + [b + a], target)

    # - 인경우 dfs 돌리기
    res2 = solution(numbers + [b - a], target)

    return res1 + res2




numbers = [1, 1, 1, 1, 1]	
target = 3
print(solution(numbers, target))