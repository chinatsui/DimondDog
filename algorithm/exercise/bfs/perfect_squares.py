"""
LeetCode-279

Given a positive integer n, find the least number
of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""


def _squares(n):
    i = 1
    squares = []
    while i ** 2 <= n:
        squares.append(i ** 2)
        i += 1
    return squares


class Solution:
    @staticmethod
    def num_squares(n):
        """
        Imagine n is the root node, and its child nodes are those of (n - square less than n).
        Our target is to repeat above operation levelly to find a node of 0.
        Then this is actually a BFS process, and the level of node 0 is the answer (root level is 0).
        """
        squares = _squares(n)
        cnt = 0
        remains = {n}
        while remains:
            cnt += 1
            tmp = set()
            for remain in remains:
                for sq in [sqq for sqq in squares if sqq <= remain]:
                    if remain == sq:
                        return cnt
                    else:
                        tmp.add(remain - sq)
            remains = tmp


class Solution2:

    @staticmethod
    def num_squares(n):
        """
        Thinking of dynamic programming, however it is not less efficient than BFS.
        """
        nums = _squares(n)

        dp = [0] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            can = [j for j in nums if j <= i]
            dp[i] = 1 + min([dp[i - c] for c in can])

        return dp[n]


print(Solution().num_squares(12))
