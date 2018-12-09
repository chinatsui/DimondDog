"""
LeetCode-123

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution:
    """
    The profit of last transaction can be understood as a cost reduce for current transaction.
    """

    @staticmethod
    def max_profit(prices):
        if not prices or len(prices) < 2:
            return 0

        cost1, cost2 = prices[0], prices[0]
        profit1, profit2 = 0, 0

        n = len(prices)
        for i in range(1, n):
            cost1 = min(cost1, prices[i])
            profit1 = max(profit1, prices[i] - cost1)
            cost2 = min(cost2, prices[i] - profit1)
            profit2 = max(profit2, prices[i] - cost2)

        return profit2


print(Solution().max_profit([3, 4, 6, 0, 0, 3, 1, 4]))
