"""
LeetCode - 58

Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""


class Solution:
    @staticmethod
    def length_of_last_word(s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0

        i = 0
        for j in range(len(s)):
            if s[j] == ' ':
                i = j + 1

        return len(s[i:])
