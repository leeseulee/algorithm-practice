import heapq

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

X, K = map(int, input().split())

INF = int(1e9)


def min_dist(start, n, graph):
    d = [INF] * (n + 1)
    visited = [False] * (n + 1)
    q = []

    d[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if visited[now]: continue
        visited[now] = True

        for c in graph[now]:
            if dist + 1 < d[c]:
                d[c] = dist + 1
                heapq.heappush(q, (dist + 1, c))

    return d


from_first = min_dist(1, N, graph)
from_k = min_dist(K, N, graph)

result = from_first[K] + from_k[X]
if result > INF:
    result = -1

print(result)