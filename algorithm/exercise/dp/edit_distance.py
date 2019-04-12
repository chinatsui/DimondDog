class EditDistance:

    @staticmethod
    def resolve(word1, word2):
        if not word1:
            return len(word2)

        if not word2:
            return len(word1)

        m, n = len(word1), len(word2)

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 0 if word1[0] == word2[0] else 1

        for i in range(1, m):
            dp[i][0] = i if word1[i] == word2[0] else dp[i - 1][0] + 1

        for j in range(1, n):
            dp[0][j] = j if word2[j] == word1[0] else dp[0][j - 1] + 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j] + 1,
                               dp[i][j - 1] + 1,
                               dp[i - 1][j - 1] if word1[i] == word2[j] else dp[i - 1][j - 1] + 1)

        return dp[m - 1][n - 1]

# print(EditDistance().resolve('a', 'ab'))
