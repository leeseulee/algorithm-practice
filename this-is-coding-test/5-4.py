from collections import deque

n, m = map(int, input().split())
l = []
for _ in range(n):
    l.append(list(map(int, input())))

visited = [[False] * m for _ in range(n)]
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
queue = deque([(0, 0)])

while queue:
    v = queue.popleft()
    if v[0] == n - 1 and v[1] == m - 1:
        break
    for d in directions:
        nx = v[0] + d[0]
        ny = v[1] + d[1]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if l[nx][ny] != 0:
            queue.append((nx, ny))
            l[nx][ny] = l[v[0]][v[1]] + 1

print(l[n - 1][m - 1])
