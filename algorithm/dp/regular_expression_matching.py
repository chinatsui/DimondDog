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
        if not s or not p:
            return False
        # The DP dp and the string s and p use the same indexes i and j, but
        # dp[i][j] means the match status between p[:i] and s[:j], i.e.
        # dp[0][0] means the match status of two empty strings, and
        # dp[1][1] means the match status of p[0] and s[0]. Therefore, when
        # referring to the i-th and the j-th characters of p and s for updating
        # dp[i][j], we use p[i - 1] and s[j - 1].

        # Initialize the dp with False. The first row is satisfied.
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        # Update the corner case of matching two empty strings.
        dp[0][0] = True

        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the dp is
        # vertically updated by the one before previous. [test_symbol_0]
        for i in range(2, len(p) + 1):
            dp[i][0] = dp[i - 2][0] and p[i - 1] == '*'

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    # Update the dp by referring the diagonal element.
                    dp[i][j] = dp[i - 1][j - 1] and \
                               (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    dp[i][j] = dp[i - 2][j] or dp[i - 1][j]

                    # Propagation (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        dp[i][j] |= dp[i][j - 1]

        return dp[-1][-1]


print(Solution().is_match('aa', 'a'))
print(Solution().is_match('aa', 'a*'))
print(Solution().is_match('ab', '.*'))
print(Solution().is_match('aab', 'c*a*b'))
print(Solution().is_match('mississippi', 'mis*is*p*.'))
