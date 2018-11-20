"""
LeetCode-494

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S.
Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""


class Solution:
    def find_target_sum_ways(self, nums, S):
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
    def find_target_sum_ways(nums, S):
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


print(Solution().find_target_sum_ways([1, 1, 1, 1, 1], 3))
print(Solution2().find_target_sum_ways([1, 1, 1, 1, 1], 3))
