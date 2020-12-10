# https://programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter
def solution(participant, completion):
    return list(Counter(participant)-Counter(completion))[0]

participant = ["leo", "kiki", "eden"]	
completion = ["eden", "kiki"]	

print(solution(participant, completion))