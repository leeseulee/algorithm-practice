import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

print(graph)

# 기본
# distance[start] = 0
# for _ in range(n):
#     visited[start] = True

#     for edge in graph[start]:
#         distance[edge[0]] = min(distance[edge[0]], distance[start] + edge[1])

#     min_node = 0
#     min_distance = INF
#     for i in range(1, n + 1):
#         if not visited[i] and distance[i] < min_distance:
#             min_node = i
#             min_distance = distance[i]

#     start = min_node

# 개선
distance[start] = 0
min_d = []
heapq.heappush(min_d, (0, start))
while min_d:
    dist, now = heapq.heappop(min_d)
    if visited[now]: continue
    visited[now] = True

    for edge in graph[now]:
        new_d = dist + edge[1]
        if new_d < distance[edge[0]]:
            distance[edge[0]] = new_d
            heapq.heappush(min_d, (new_d, edge[0]))

print(distance)