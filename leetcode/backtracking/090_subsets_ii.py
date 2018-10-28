class Solution:
    def subsetsWithDup(self, nums):
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


print(Solution().subsetsWithDup([1, 2, 2]))
