class Knapsack01:

    def __init__(self, item_weights, item_values):
        self.w = item_weights
        self.v = item_values

    def max_value(self, capacity):
        """
        Define dp[n+1][v+1], then dp[i][j] refers to max value of the first i elements in capacity of j.
        To calculate dp[i][j], we should compare j with w[i] first to see if we can include element i.
        If j < w[i], then we cannot put the element i, so:
            dp[i][j] = dp[i-1][j]
        If j > w[i], then we have choice to put element i or not, so:
            dp[i][j] = max of:
                (a) dp[i-1][j-w[i]] + v[i];
                (b) dp[i-1][j];
        Eventually, we return dp[n][v] as answer.
        """
        n = len(self.v)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, capacity + 1):
                if j > self.w[i - 1]:
                    dp[i][j] = max(dp[i - 1][j - self.w[i - 1]] + self.v[i - 1], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][capacity]


solution = Knapsack01([2, 2, 6, 5, 4], [6, 3, 5, 4, 6])
print(solution.max_value(10))
