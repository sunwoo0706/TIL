# https://programmers.co.kr/learn/courses/30/lessons/60057
# 2020 카카오 블라인드채용 
# 구현
def solution(s):
    answer = int(1e9)
    for i in range(1, len(s)+1):
        save = ""
        prev = ""
        n = 1
        for j in range(0, len(s), i):
            if prev == s[j:j+i]:
                n += 1
            else:
                if n > 1:
                    save += str(n)+prev
                else:
                    save += prev
                prev = s[j:j+i]
                n = 1

        if n > 1:
            save += str(n)+prev
        else:
            save += prev
        
        answer = min(answer, len(save))

    return answer8




            

s = "aabbaccc"	
# s = "ababcdcdababcdcd"	
# s = "abcabcdede"
# s = "abcabcabcabcdededededede"
# s = "xababcdcdababcdcd"
print(solution(s))