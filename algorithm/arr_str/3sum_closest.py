"""
Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    """
    Thought is similar to 3sum, nothing special.
    """

    def three_sum_closest(self, nums, target):
        nums = sorted(nums)
        min_diff = None
        res = None
        for i in range(len(nums) - 2):
            (arr, diff) = self._two_sum_closest(nums, i + 1, len(nums) - 1, target - nums[i])
            if diff == 0:
                return target
            elif not min_diff or min_diff > abs(diff):
                min_diff = abs(diff)
                res = [nums[i], arr[0], arr[1]]

        return sum(res)

    @staticmethod
    def _two_sum_closest(nums, lo, hi, target):
        local = None
        arr = None

        while lo < hi:
            diff = target - nums[lo] - nums[hi]
            if diff == 0:
                arr = [nums[lo], nums[hi]]
                return arr, diff
            elif not local or local > abs(diff):
                local = abs(diff)
                arr = [nums[lo], nums[hi]]

            if diff < 0:
                hi -= 1
            else:
                lo += 1

        return arr, local
