"""
LeetCode-367

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
Input: 16
Output: true

Example 2:
Input: 14
Output: false
"""


class Solution:
    @staticmethod
    def is_perfect_square(num):
        lo, hi = 0, num
        while lo < hi:
            mid = (lo + hi) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                lo = mid + 1
            else:
                hi = mid
        return True if lo ** 2 == num else False
