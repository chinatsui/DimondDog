"""
LeetCode - 168

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...

Example 1:
Input: 1
Output: "A"

Example 2:
Input: 28
Output: "AB"

Example 3:
Input: 701
Output: "ZY"
"""


class Solution:
    @staticmethod
    def convert_to_title(n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n > 26:
            mod = n % 26
            n = n // 26
            if mod != 0:
                res = chr(64 + mod) + res
            else:
                res = 'Z' + res
                n -= 1
        return chr(64 + n) + res


print(Solution().convert_to_title(52))
