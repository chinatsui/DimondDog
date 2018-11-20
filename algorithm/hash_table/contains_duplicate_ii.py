"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""


class Solution:
    @staticmethod
    def contains_nearby_duplicate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False

        diff = len(nums)
        num_idx_map = dict()

        for (i, n) in enumerate(nums):
            if n in num_idx_map:
                diff = min(diff, i - num_idx_map[n])
                if diff <= k:
                    return True
                num_idx_map[n] = i
            else:
                num_idx_map[n] = i
        return False
