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
    """
    Hash Table + sliding window.
    We can understand "difference between nums[i] and nums[j] is at most t" as nums[i] "equals" nums[j] as long as
    diff between them is less equal than t. How to express it using program? See below:
            1) nums[i] / (t + 1) == nums[j] / (t + 1)
            2) nums[i] / (t + 1) == nums[j] / (t + 1) + 1 and abs(nums[i] - nums[j]) < t + 1
            3) nums[i] / (t + 1) + 1 == nums[j] / (t + 1) and abs(nums[i] - nums[j]) < t + 1
    So use a cache to store "nums[i] / (t + 1)" -> nums[i] for each time, and check above rule in each sliding window.
    """

    @staticmethod
    def contains_nearby_almost_duplicate(nums, k, t):
        if t < 0:
            return False

        cache = {}
        w = t + 1  # why t + 1, because if t == 0, then 0 cannot be as divisor
        for (i, n) in enumerate(nums):
            m = n // w

            if m in cache:
                return True

            if m - 1 in cache and abs(n - cache[m - 1]) < w:
                return True

            if m + 1 in cache and abs(n - cache[m + 1]) < w:
                return True

            cache[m] = n

            if i >= k:
                del cache[nums[i - k] // w]
        return False


print(Solution().contains_nearby_almost_duplicate([1, 5, 9, 1, 5, 9], k=2, t=3))
