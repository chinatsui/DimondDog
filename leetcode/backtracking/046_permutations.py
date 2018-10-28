"""
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
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
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


class Solution2:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list()
        self._backtrack(list(), res, set(nums), len(nums))
        return res

    def _backtrack(self, cur, res, candidates, end):
        if len(cur) == end:
            res.append(cur)
            return

        for i in candidates:
            self._backtrack(cur + [i], res, candidates - set([i]), end)


print(Solution().permute([1, 2, 3]))
print(Solution2().permute([1, 2, 3]))
