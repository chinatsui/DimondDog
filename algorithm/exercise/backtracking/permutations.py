"""
LeetCode-46

Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:
    def permute(self, nums):
        res = []
        self._backtrack([], res, nums, [False] * len(nums))
        return res

    def _backtrack(self, cur, res, nums, is_used):
        if len(cur) == len(nums):
            res.append(cur)
            return

        for i in range(0, len(nums)):
            if not is_used[i]:
                is_used[i] = True
                self._backtrack(cur + [nums[i]], res, nums, is_used)
                is_used[i] = False


print(Solution().permute([1, 2, 3]))
