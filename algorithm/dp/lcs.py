class LongestCommonSubSequence:

    @staticmethod
    def count_LCS(seq_a, seq_b):
        """
        Given:
            sequence X: X[1...n-1]X[n]
            sequence Y: Y[1...m-1]Y[m]

        if x[n] == x[m], then LCS(X[1...n], Y[1...m]) = LCS(X[1...n-1], Y[1...m-1]) + X[n] or Y[m]
        if x[n] != x[m], then LCS(X[1...n], Y[1...m]) = max(LCS(X[1...n-1]Y[1...m]), LCS(X[1...n],Y[1...m-1]))

        To avoid repetitive count, we start from X[0], Y[0] onwards to count one by one in a bi-loop.
        """
        if not seq_a or not seq_b:
            return 0

        m, n = len(seq_a), len(seq_b)
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            dp[i][0] = 1 if seq_a[i] == seq_b[0] else 0

        for j in range(n):
            dp[0][j] = 1 if seq_a[0] == seq_b[j] else 0

        for i in range(1, m):
            for j in range(1, n):
                if seq_a[i] == seq_b[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m - 1][n - 1]


solution = LongestCommonSubSequence()
t_seq_a = 'abbbcccdef'
t_seq_b = 'malnbbcccdxyz'
print(solution.count_LCS(t_seq_a, t_seq_b))
