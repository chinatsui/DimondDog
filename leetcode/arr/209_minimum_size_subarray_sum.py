class Solution:
    @staticmethod
    def min_sub_array_len(s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i, j, n = 0, 0, len(nums)
        res = float('inf')
        sum_val = 0
        for j in range(n):
            sum_val += nums[j]
            while sum_val >= s:
                res = min(res, j - i + 1)
                sum_val -= nums[i]
                i += 1
            j += 1
        return res if res != float('inf') else 0
