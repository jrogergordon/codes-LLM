def count_squares(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    count = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                count += dp[i][j]

    return count

matrix = [[1,1,1,0],
          [1,1,1,1],
          [1,1,1,0],]
k=3
print(count_squares(matrix))