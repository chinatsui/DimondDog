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


class Solution:
    def num_squares(self, n):
        """
        Imagine n is the root node, and its child nodes are those of (n - square less than n).
        Our target is to repeat above operation levelly to find a node of 0.
        Then this is actually a BFS process, and the level of node 0 is the answer (root level is 0).
        """
        squares = self._squares(n);
        cnt = 0
        remains = {n}
        while remains:
            cnt += 1
            tmp = set()
            for remain in remains:
                for sq in squares:
                    if remain < sq:
                        break
                    elif remain == sq:
                        return cnt
                    else:
                        tmp.add(remain - sq)
            remains = tmp

    @staticmethod
    def _squares(n):
        i = 1
        squares = []
        while i ** 2 <= n:
            squares.append(i ** 2)
            i += 1
        return squares


print(Solution().num_squares(12))
