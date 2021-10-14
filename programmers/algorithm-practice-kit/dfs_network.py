def dfs(i, computers, visited):
    visited[i] = True
    for j in range(len(visited)):
        if i != j and computers[i][j] == 1 and not visited[j]:
            dfs(j, computers, visited)


def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i]: continue
        dfs(i, computers, visited)
        answer += 1
    return answer