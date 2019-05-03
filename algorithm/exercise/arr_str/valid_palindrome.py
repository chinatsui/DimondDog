"""
LeetCode-125

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
"""


class Solution(object):
    @staticmethod
    def is_palindrome(s):
        if not s:
            return True

        lo, hi, ch_arr = 0, len(s) - 1, '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        while lo < hi:
            lo_str, hi_str = s[lo].upper(), s[hi].upper()

            if lo_str not in ch_arr:
                lo += 1
                continue

            if hi_str not in ch_arr:
                hi -= 1
                continue

            if lo_str != hi_str:
                return False

            lo += 1
            hi -= 1

        return True
