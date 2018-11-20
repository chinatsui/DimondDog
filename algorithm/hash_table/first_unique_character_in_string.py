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

from collections import OrderedDict


class Solution:
    @staticmethod
    def first_uniq_char(s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1

        seen = set()
        ch_idx_map = OrderedDict()

        for (i, ch) in enumerate(s):
            if ch not in seen:
                seen.add(ch)
                ch_idx_map[ch] = i
            else:
                if ch in ch_idx_map:
                    ch_idx_map.pop(ch)

        return list(ch_idx_map.values())[0] if ch_idx_map else -1


print(Solution().first_uniq_char("leetcode"))
