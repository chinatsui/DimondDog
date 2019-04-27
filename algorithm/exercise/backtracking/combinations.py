"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution:
    def combine(self, n, k):
        if n < 1:
            return []

        nums = [i for i in range(1, n + 1)]

        if k > len(nums):
            return []

        res = []
        self.backtrack(nums, k, res, [], 0)
        return res

    def backtrack(self, nums, k, res, cur, i):
        if len(cur) == k:
            res.append(cur)
            return

        for j in range(i, len(nums)):
            self.backtrack(nums, k, res, cur + [nums[j]], j + 1)
