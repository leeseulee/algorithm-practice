def find(parent, v):
    if parent[v] == v:
        return v
    else:
        return find(parent, parent[v])


def find(parent, v):
    if parent[v] != v:
        parent[v] = find(parent, parent[v])
    return parent[v]


def union(parent, a, b):
    a_parent = find(parent, a)
    b_parent = find(parent, b)
    if a_parent < b_parent:
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent


v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b = map(int, input().split())
    union(parent, a, b)

print(parent)

# 사이클 판별 (무방향 그래프만 가능)
cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find(parent, a) == find(parent, b):
        cycle = True
        break
    else:
        union(parent, a, b)

print(cycle)