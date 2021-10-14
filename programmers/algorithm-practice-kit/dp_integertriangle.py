def solution(t):
    dp = [[0] * len(t[i]) for i in range(len(t))]
    dp[-1] = t[-1]
    for i in range(len(t) - 2, -1, -1):
        for j in range(len(t[i])):
            dp[i][j] = max(t[i][j] + dp[i + 1][j], t[i][j] + dp[i + 1][j + 1])
    return dp[0][0]