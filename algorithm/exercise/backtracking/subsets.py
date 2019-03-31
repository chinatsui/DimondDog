"""
LeetCode-78

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self._backtrack([], res, nums, 0)
        return res

    def _backtrack(self, cur, res, nums, start):
        res.append(cur)
        if start == len(nums):
            return
        for i in range(start, len(nums)):
            self._backtrack(cur + [nums[i]], res, nums, i + 1)


print(Solution().subsets([1, 2, 3]))
