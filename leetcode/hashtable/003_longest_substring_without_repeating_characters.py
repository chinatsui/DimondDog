class Solution:
    def length_of_longest_substring(self, s):
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
