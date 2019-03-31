"""
Given a string and a number k. The string may contains some deduplicate characters, if count of deduplication is more
than k, then remove redundant ones.

Example:
Input: abaacccddefdacxyzaaa, k = 3
Output: abaacccddefdxyz
"""


class Solution:

    @staticmethod
    def remove_redundant(s, k):
        if not s or k == 0:
            return ''

        cnt_map = dict()
        i, j, n = 0, 0, len(s)
        seq_list = []
        while j < n:
            cnt = cnt_map.get(s[j], 0)
            if cnt == k:
                seq_list.append(s[i:j])
                i = j + 1
            else:
                cnt_map[s[j]] = cnt + 1
            j += 1
        return ''.join(seq_list)


print(Solution().remove_redundant('abaacccddefdacxyzaaa', 3))
