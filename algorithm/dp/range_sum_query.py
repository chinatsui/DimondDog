"""
LeetCode-303

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""


class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            return

        n = len(nums)
        self.dp = [0] * n
        self.dp[0] = nums[0]
        for i in range(1, n):
            self.dp[i] = nums[i] + self.dp[i - 1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.dp:
            return 0

        if i == 0:
            return self.dp[j]
        else:
            return self.dp[j] - self.dp[i - 1]


solution = NumArray([-2, 0, 3, -5, 2, -1])
print(solution.sumRange(0, 2))
print(solution.sumRange(2, 5))
print(solution.sumRange(0, 5))
