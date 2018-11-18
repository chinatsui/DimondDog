"""
LeetCode-34

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

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
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        start_idx = self._find_left_most(nums, target)
        if start_idx == -1:
            return [-1, -1]
        end_idx = self._find_right_most(nums, target)
        return [start_idx, end_idx]

    @staticmethod
    def _find_left_most(nums, target):
        lo, hi = 0, len(nums) - 1
        res = -1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                res = mid
                hi = mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        if nums[lo] == target:
            res = lo
        return res

    @staticmethod
    def _find_right_most(nums, target):
        lo, hi = 0, len(nums) - 1
        res = -1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                res = mid
                lo = mid + 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        if nums[lo] == target:
            res = lo
        return res


print(Solution().search_range([5, 7, 7, 8, 8, 10], 8))
