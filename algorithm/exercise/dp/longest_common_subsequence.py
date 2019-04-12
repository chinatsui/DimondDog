class LongestCommonSubsequence:

    @staticmethod
    def resolve(seq1, seq2):
        if not seq1 or not seq2:
            return 0

        m, n = len(seq1), len(seq2)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1 if seq1[0] == seq2[0] else 0

        for j in range(1, n):
            dp[0][j] = 1 if seq1[0] == seq2[j] else dp[0][j - 1]

        for i in range(1, m):
            dp[i][0] = 1 if seq1[i] == seq2[0] else dp[i - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                if seq1[i] == seq2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m - 1][n - 1]

# print(LongestCommonSubsequence().resolve('ayybyyc', 'axxxbxxxxc'))
