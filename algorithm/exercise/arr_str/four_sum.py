"""
LeetCode-18

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums
such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []

        for i in range(len(nums) - 3):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            three_sum_res = self._three_sum(nums, i + 1, target - nums[i])
            for entry in three_sum_res:
                res.append([nums[i]] + entry)
        return res

    def _three_sum(self, nums, start, target):
        res = []

        for i in range(start, len(nums) - 2):
            if i > start and nums[i - 1] == nums[i]:
                continue

            two_sum_res = self._two_sum(nums, i + 1, target - nums[i])
            for entry in two_sum_res:
                res.append([nums[i]] + entry)
        return res

    @staticmethod
    def _two_sum(nums, start, target):
        res = []

        lo, hi = start, len(nums) - 1
        while lo < hi:
            sum = nums[lo] + nums[hi]
            if sum < target:
                lo += 1
            elif sum > target:
                hi -= 1
            else:
                res.append([nums[lo], nums[hi]])
                while lo < hi and nums[lo] == nums[lo + 1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi - 1]:
                    hi -= 1
                lo += 1
                hi -= 1
        return res
