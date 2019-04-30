"""
Given: "16.16.0.0", convert it to an 32 bits integer, its binary representation
is like "00010000 00010000 000000000 000000000"
"""


class Solution:

    def convert(self, s):
        if not s:
            return 0

        nums = self.get_numbers(s)
        res, n = 0, 3
        for (i, num) in enumerate(nums):
            res += pow(2, (n - i) * 8) * num
        return res

    @staticmethod
    def get_numbers(s):
        nums = []
        i, j = 0, -1
        for i in range(len(s)):
            if s[i] == '.':
                nums.append(int(s[j + 1:i]))
                j = i
        nums.append(int(s[j + 1:]))
        return nums


print(Solution().convert('0.0.2.15'))
