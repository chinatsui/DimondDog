"""
LeetCode-205

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""


class Solution:
    def is_isomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        return self._transform(s) == self._transform(t)

    @staticmethod
    def _transform(var):
        res = ''
        ch_map = dict()
        mark = 0
        for ch in var:
            if ch in ch_map:
                res += ch_map[ch]
            else:
                ch_map[ch] = str(mark)
                mark += 1
        return res
