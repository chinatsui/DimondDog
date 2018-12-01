"""
CC150-9.8
Given some coins with different denominations: 1, 5, 10, 25.
We need to make change for 100, hwo many ways to do it?
"""


class Solution:
    """
    A rapid thought for this problem is to do dfs as below:
             []
            /
           25
         / | \ \
       25 10  5 1
      /
     25

    However, above approach would include a lot of duplicate combinations, and it is very hard to do deduplication.
    An improved solution is to limit what coin to select for next layer, as below:

        25*0 25*1 25*2 25*3 25*4 ... 25*i <=n
       /
     10*0 ... 10*j <= n - 25*i

    When coin is 1, then we reach the end and just return 1. (Think it why?)
    """

    def make_change(self, n):
        return self._dfs(n, 25)

    def _dfs(self, n, denom):
        if denom == 25:
            next_denom = 10
        elif denom == 10:
            next_denom = 5
        elif denom == 5:
            next_denom = 1
        elif denom == 1:
            return 1

        i = 0
        ways = 0
        while denom * i <= n:
            ways += self._dfs(n - denom * i, next_denom)
            i += 1

        return ways
