class Solution:
    @staticmethod
    def longest_palindrome(s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        res = s[0]
        for j in range(1, n):
            for i in range(0, j):
                if i + 1 < j:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j]

                if dp[i][j] and (j - i + 1) > len(res):
                    res = s[i:j + 1]
        return res


print(Solution().longest_palindrome('babad'))
