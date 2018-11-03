class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        return self._dfs(nums, 0, 0, S, {})

    def _dfs(self, nums, i, sum, target, cache):
        if i == len(nums):
            if sum == target:
                return 1
            else:
                return 0

        key = (i, sum)
        if key in cache:
            return cache[key]

        plus_cnt = self._dfs(nums, i + 1, sum + nums[i], target, cache)
        minus_cnt = self._dfs(nums, i + 1, sum - nums[i], target, cache)
        cache[key] = plus_cnt + minus_cnt
        return plus_cnt + minus_cnt


class Solution2(object):
    @staticmethod
    def findTargetSumWays(nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sum_val = sum(nums)
        if sum_val < S or (sum_val + S) % 2 == 1:
            return 0

        p = (sum_val + S) // 2
        dp = [0] * (p + 1)
        dp[0] = 1

        for n in nums:
            for i in range(p, n - 1, -1):
                dp[i] += dp[i - n]
        return dp[p]


print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
print(Solution2().findTargetSumWays([1, 1, 1, 1, 1], 3))
