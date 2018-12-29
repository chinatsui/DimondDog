"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321
Example 2:

Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−2^31, 2^31 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    @staticmethod
    def reverse(x):
        is_negative = x < 0
        x = abs(x)
        res = 0
        while x > 0:
            mod = x % 10
            x = x // 10
            res = res * 10 + mod

        if is_negative:
            res = - res

        if res > pow(2, 31) - 1:
            return 0

        if res < -pow(2, 31):
            return 0

        return res


print(Solution().reverse(1534236469))
