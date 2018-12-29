"""
LeetCode-387

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""


class Solution:
    @staticmethod
    def first_unique_char(s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1

        ch_idx_map = dict()

        for (i, ch) in enumerate(s):
            if ch not in ch_idx_map:
                ch_idx_map[ch] = i
            else:
                del ch_idx_map[ch]

        return list(ch_idx_map.values())[0] if ch_idx_map else -1


print(Solution().first_unique_char("loveleetcode"))
