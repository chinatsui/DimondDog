"""
LeetCode-3

Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    """
    This problem is a good example to compare with "Longest Increasing Subsequence".
    This one requires a contiguous subsequence, but that one doesn't. Think the difference over and over.
    """

    @staticmethod
    def length_of_longest_substring(s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        ch_set = set()

        count = 0
        i = j = 0
        while j < len(s):
            if s[j] in ch_set:
                ch_set.remove(s[i])
                i += 1
            else:
                ch_set.add(s[j])
                count = max(count, len(ch_set))
                j += 1
        return count


print(Solution().length_of_longest_substring('abcabcbb'))
