import heapq


def solution(n, edge):
    graph = [[] for _ in range(n)]
    for e in edge:
        graph[e[0] - 1].append(e[1] - 1)
        graph[e[1] - 1].append(e[0] - 1)

    d = [n] * n
    visited = [False] * n
    q = []

    d[0] = 0
    heapq.heappush(q, (0, 0))

    while q:
        dist, now = heapq.heappop(q)
        if visited[now]: continue
        visited[now] = True
        for node in graph[now]:
            if dist + 1 < d[node]:
                d[node] = dist + 1
                heapq.heappush(q, (dist + 1, node))

    return d.count(max(d))