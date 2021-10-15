import heapq


def find(parent, v):
    if parent[v] != v:
        parent[v] = find(parent, parent[v])
    return parent[v]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

q = []
total = 0
for _ in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(q, (c, (a, b)))

while q:
    cost, now = heapq.heappop(q)
    a = find(parent, now[0])
    b = find(parent, now[1])
    if a != b:
        union(parent, now[0], now[1])
        total += cost

print(total)