"""
LeetCode-10

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


class Solution:
    """
    1, If p.charAt(j) == s.charAt(i) :  dp[i][j] = dp[i-1][j-1];
    2, If p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1];
    3, If p.charAt(j) == '*':
       here are two sub conditions:
                   1   if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2]  //in this case, a* only counts as empty
                   2   if p.charAt(j-1) == s.charAt(i) or p.charAt(j-1) == '.':
                                  dp[i][j] = dp[i-1][j]    // in this case, a* counts as multiple a
                               or dp[i][j] = dp[i][j-1]    // in this case, a* counts as single a
                               or dp[i][j] = dp[i][j-2]    // in this case, a* counts as empty
    """

    @staticmethod
    def is_match(s, p):
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(2, n + 1):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != '*':
                    dp[i][j] = dp[i - 1][j - 1] and (p[j - 1] == s[i - 1] or p[j - 1] == '.')
                else:
                    # a* counts as empty or single a
                    dp[i][j] = dp[i][j - 2] or dp[i][j - 1]

                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        # a* counts as multiple a
                        dp[i][j] |= dp[i - 1][j]

        return dp[m][n]


print(Solution().is_match('aa', '*'))
# print(Solution().is_match('aa', 'a'))
# print(Solution().is_match('aa', 'a*'))
# print(Solution().is_match('ab', '.*'))
# print(Solution().is_match('aab', 'c*a*b'))
# print(Solution().is_match('mississippi', 'mis*is*p*.'))
