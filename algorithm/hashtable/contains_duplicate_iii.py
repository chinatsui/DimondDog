"""
LeetCode-220

Given an array of integers, find out whether there are two distinct indices i and j in the array
such that the absolute difference between nums[i] and nums[j] is at most t
and the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
"""


class Solution:

    @staticmethod
    def contains_nearby_almost_duplicate(nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False

        d = {}
        w = t + 1
        for (i, n) in enumerate(nums):
            m = n // w

            if m in d:
                return True

            if m - 1 in d and abs(n - d[m - 1]) < w:
                return True

            if m + 1 in d and abs(n - d[m + 1]) < w:
                return True

            d[m] = n

            if i >= k:
                del d[nums[i - k] // w]
        return False


print(Solution().contains_nearby_almost_duplicate([1, 5, 9, 1, 5, 9], k=2, t=3))
