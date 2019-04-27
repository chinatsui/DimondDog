class MakeMoneyChanges:
    """
    Given several coins with different denominations: c[0]...c[i],
    output the smallest coins to make changes of money.

    Example:
    Given: coins = [1,3,5], money = 9
    Output: 3
    Explanation: 9 = 3+3+3 or 1+3+5
    """

    @staticmethod
    def resolve(coins, money):
        """
        dp[i] = 1 + min([dp[i - j]), j in the coins where value is less than i
        """
        coins = sorted(coins)
        dp = [-1 for _ in range(money + 1)]
        dp[0] = 0
        for i in range(1, money + 1):
            options = []
            for c in coins:
                if i >= c and dp[i - c] > -1:
                    options.append(dp[i - c])
                elif i < c:
                    break
            if options:
                dp[i] = 1 + min(options)

        return dp[money]

# print(MakeMoneyChanges().resolve([2, 3, 5], 9))
