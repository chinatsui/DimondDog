class MatrixShortestPath:

    @staticmethod
    def resolve(matrix):
        """
        dp[i][j] == min(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
        """
        if not matrix or not matrix[0]:
            return -1

        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = matrix[0][0]

        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + matrix[0][j]

        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + matrix[i][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]

        return dp[m - 1][n - 1]

# print(MatrixShortestPath().resolve([
#     [1, 3, 5, 9],
#     [2, 1, 3, 4],
#     [5, 2, 6, 7],
#     [6, 8, 4, 3],
# ]))
