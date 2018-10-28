"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)  # very important for duplicated element skip
        self._backtrack([], res, nums, [False] * len(nums))
        return res

    def _backtrack(self, cur, res, nums, is_used):
        if len(cur) == len(nums):
            res.append(list(cur))
            return

        for i in range(0, len(nums)):
            if is_used[i] or i > 0 and nums[i - 1] == nums[i] and not is_used[i - 1]:
                continue
            is_used[i] = True
            self._backtrack(cur + [nums[i]], res, nums, is_used)
            is_used[i] = False


print(Solution().permuteUnique([3, 3, 0, 3]))
