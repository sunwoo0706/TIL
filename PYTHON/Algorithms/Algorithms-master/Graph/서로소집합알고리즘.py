# 루트 노드를 찾기 위해 부모 테이블을 계속해서 확인하며 거슬러 올라간다. (기본적인 서로소집합 알고리즘)
def find_parent_basic(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 경로 압축 알고리즘
# 재귀적으로 호출하고, 부모 테이블의 값을 바로 갱신한다.
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

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end=' ')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')
print()

print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')


# 6 4
# 1 4
# 2 3
# 2 4
# 5 6
