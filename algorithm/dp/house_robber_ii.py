"""
You are a professional robber planning to rob houses along a street.

Each house has a certain amount of money stashed. All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.

Meanwhile, adjacent houses have security system connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.

Example 2:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""


class Solution:
    """
    Think that we can choose to rob the range of houses.
    Then the answer is Math.max(rob(0...n-2), rob(1...n-1))
    """

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        if n < 2:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        return max(self.rob_range(nums, 0, n - 2), self.rob_range(nums, 1, n - 1))

    @staticmethod
    def rob_range(nums, lo, hi):
        if lo == hi:
            return nums[lo]

        if lo + 1 == hi:
            return max(nums[lo], nums[hi])

        dp = [0] * (hi - lo + 1)
        dp[0] = nums[lo]
        dp[1] = max(nums[lo], nums[lo + 1])

        for i in range(lo + 2, hi + 1):
            j = i - lo
            dp[j] = max(dp[j - 1], dp[j - 2] + nums[i])

        return dp[hi - lo]
