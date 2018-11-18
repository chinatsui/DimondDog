"""
LeetCode-90

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution:
    def subsets_with_dup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        self._backtrack([], res, nums, 0)
        return res

    def _backtrack(self, cur, res, nums, start):
        res.append(cur)

        if start == len(nums):
            return

        for i in range(start, len(nums)):
            if i > start and nums[i - 1] == nums[i]:
                continue
            self._backtrack(cur + [nums[i]], res, nums, i + 1)


print(Solution().subsets_with_dup([1, 2, 2]))
