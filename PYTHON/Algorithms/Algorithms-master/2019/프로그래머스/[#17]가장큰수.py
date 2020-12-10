# from itertools import permutations

# def solution(numbers):
# 	arr = list(permutations(numbers))
# 	arr = [[str(col) for col in row] for row in arr]
# 	arr = list(map(lambda x : ''.join(x), arr))
# 	return max(arr)


def solution(numbers):
    numbers = list(map(str, numbers))
    print(numbers)
    numbers.sort(key=lambda x: x*3, reverse=True)
    print(numbers)
    return str(int(''.join(numbers)))


# 문자열 비교연산의 경우엔 첫번째 인덱스인 666[0]인 6과 101010[0]인 1과 222[0]인 2를 ascii숫자로 바꿔서 비교합니다. 물론 같으면, 다음 인덱스도 비교합니다. 비교한 결과 [6, 2, 10]의 순으로 정렬됩니다.


print(solution([3, 30, 34, 5, 9]))