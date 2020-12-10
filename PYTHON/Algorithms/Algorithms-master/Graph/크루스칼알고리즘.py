# 크루스칼 - 최소신장트리 구하기 (greedy)

# 경로 압축 알고리즘 : 재귀적으로 호출하고, 부모 테이블의 값을 바로 갱신한다.
# 특정한 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

edges = [] # 모든 간선을 담을 리스트
result = 0 # 최종 비용을 담을 변수

for i in range(1, v+1):
    parent[i] = i



for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b)) 

# 비용순으로 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge

    # 사이클이 발생하지 않은 경우 합치기
    if find_parent(parent, a) != find_parent(parent, b): 
        union_parent(parent, a, b)
        result += cost

print(result)

# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25