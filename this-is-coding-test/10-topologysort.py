from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v + 1)
edges = [[] * (v + 1) for _ in range(v + 1)]
visited = [False] * (v + 1)

for _ in range(e):
    a, b = map(int, input().split())
    edges[a].append(b)
    indegree[b] += 1

q = deque()
result = []

for i in range(1, v + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    result.append(node)
    for i in edges[node]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(result)