"""
Input: 'ab  c d e'.
Output: 'abcde'
"""


class Solution:

    @staticmethod
    def remove_blank(s):
        if not s:
            return s

        i = s.index(' ')
        j = i - 1

        s = list(s)
        i += 1
        for k in range(i, len(s)):
            if s[k] != ' ':
                j += 1
                s[j], s[k] = s[k], s[j]

        return ''.join(s[0:j + 1])


print(Solution().remove_blank('    a b s  c d e  asdf    '))
