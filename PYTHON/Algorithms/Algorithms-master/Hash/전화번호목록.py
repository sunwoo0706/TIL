# https://programmers.co.kr/learn/courses/30/lessons/42577

# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.


def solution(phone_book):
    phone_book.sort()

    for i, j in zip(phone_book, phone_book[1:]):
        if j.startswith(i):
            return False

    return True


phone_book = ["119", "97674223", "1195524421"]	
print(solution(phone_book))