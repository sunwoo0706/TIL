# https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    d = {}
    a = []
    for i in range(len(genres)):
        if genres[i] in d.keys():
                d[genres[i]] += plays[i]
        else:
            d[genres[i]] = plays[i]
       
        a.append((i, genres[i], plays[i]))
    
    d = [x[0] for x in sorted(d.items(), reverse=True, key=lambda x:x[1])]
  
    a = sorted(a, key=lambda x: ([x[1] in k for k in d],x[2] ), reverse=True)

    answer = []
    c = {}
    for x in a:
        if x[1] in c.keys():
            c[x[1]] += 1
        else:
            c[x[1]] = 1
        if c[x[1]] > 2:
            continue 
        answer.append(x[0])

    return answer




genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 300, 150, 800, 2500]	

print(solution(genres, plays))