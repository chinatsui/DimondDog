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

    def _dfs(self, n, coin):
        if coin == 25:
            next_coin = 10
        elif coin == 10:
            next_coin = 5
        elif coin == 5:
            next_coin = 1
        elif coin == 1:
            return 1

        i = 0
        ways = 0
        while coin * i <= n:
            ways += self._dfs(n - coin * i, next_coin)
            i += 1

        return ways
