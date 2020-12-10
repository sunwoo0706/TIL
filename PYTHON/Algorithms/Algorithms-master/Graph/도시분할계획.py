
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

parent = [0] * (n+1)
edges = []
result = 0

# 부모노드 초기화
for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b)) # cost가 앞에 오도록

edges.sort() # cost 순으로 정렬

max_value = 0
for edge in edges:
    cost, a, b = edge

    # 크루스칼 알고리즘 : 사이클이 발생하지 않은면 합친다.
    if find_parent(parent, a) !=  find_parent(parent, b):
        max_value = max(max_value, cost)
        union_parent(parent, a, b)
        result += cost

print(result - max_value)

# 7 12
# 1 2 3
# 1 3 2 
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 5 4 1
# 6 5 3
# 4 5 3
# 6 7 4






