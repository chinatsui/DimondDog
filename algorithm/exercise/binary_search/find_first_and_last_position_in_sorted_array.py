"""
LeetCode-34

Given an array of integer nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


class Solution:
    def search_range(self, nums, target):
        if not nums:
            return [-1, -1]

        left = self._find_most(nums, target, 0)
        if left == -1:
            return [-1, -1]
        right = self._find_most(nums, target, 1)
        return [left, right]

    @staticmethod
    def _find_most(nums, target, direction):
        # direction: 0 - left, 1 = right
        lo, hi = 0, len(nums) - 1

        res = -1
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if nums[mi] < target:
                lo = mi + 1
            elif nums[mi] > target:
                hi = mi
            else:
                if direction == 0:
                    res = hi = mi
                else:
                    res, lo = mi, mi + 1

        if nums[lo] == target:
            res = lo

        return res


print(Solution().search_range([5, 7, 7, 8, 8, 10], 8))
