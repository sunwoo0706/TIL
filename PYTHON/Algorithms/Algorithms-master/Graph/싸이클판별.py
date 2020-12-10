# 서로소 집합을 이용한 사이클 판별 
# 무방향 그래프의 사이클 판별은 서로소 집합을 이용한다. (방향 그래프의 사이클 판별은 dfs)


# 경로 압축 알고리즘 : 재귀적으로 호출하고, 부모 테이블의 값을 바로 갱신한다.
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

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i


cycle = False

for i in range(e):
    a, b = map(int, input().split())

    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b): # 이미 연결되어 있는 경우 또 연결하려고 하면 사이클 발생
        cycle = True
        break
    else:
        union_parent(parent, a, b)

print(cycle)

# 3 3
# 1 2 
# 1 3
# 2 3