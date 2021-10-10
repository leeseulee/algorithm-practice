def dfs(graph, row, col, visited):
    visited[row][col] = True
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for d in direction:
        nrow = row + d[0]
        ncol = col + d[1]
        if nrow < 0 or nrow >= len(graph) or ncol < 0 or ncol >= len(
                graph[row]):
            continue
        if graph[nrow][ncol] == 0 and not visited[nrow][ncol]:
            dfs(graph, nrow, ncol, visited)


n, m = map(int, input().split())
l = []
for _ in range(n):
    l.append(list(map(int, input())))

visited = [[False] * m for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m):
        if l[i][j] == 0 and not visited[i][j]:
            dfs(l, i, j, visited)
            answer += 1