"""
LeetCode-188

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:
Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""


class Solution:
    """
    The profit of all previous transactions can be understood as a cost reduce for current transaction.
    dp[k][i] = max(dp[k][i-1], prices[i] - kth_cost)
    kth_cost = min(lowest_cost, prices[i] - all_previous_transactions_profit),
    Note: remember to update kth_cost to lowest_cost
    """

    @staticmethod
    def max_profit(k, prices):
        if k < 1 or not prices:
            return 0

        n = len(prices)
        dp = [[0] * n for _ in range(k + 1)]
        for kk in range(1, k + 1):
            cost = prices[0]
            for i in range(1, n):
                cost = min(cost, prices[i] - dp[kk - 1][i - 1])
                dp[kk][i] = max(dp[kk][i - 1], prices[i] - cost)

        return dp[k][n - 1]


print(Solution.max_profit(2, [3, 3, 5, 0, 0, 3, 1, 4]))
