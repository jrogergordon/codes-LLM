def findShortest(s):
    n = len(s)
    if (n == 0):
        return 0
    dp = [[0 for x in range(n + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if (s[i - 1] == s[j - 1] and i != j):
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j] + 1)
    return dp[n][n]