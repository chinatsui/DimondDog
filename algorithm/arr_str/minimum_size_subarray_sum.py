"""
LeetCode-209

Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum ≥ s.
If there isn't one, return 0 instead.

Example:
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
"""


class Solution:
    @staticmethod
    def min_sub_array_len(s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i, j, n = 0, 0, len(nums)
        res = float('inf')
        sum_val = 0
        for j in range(n):
            sum_val += nums[j]
            while sum_val >= s:
                res = min(res, j - i + 1)
                sum_val -= nums[i]
                i += 1
            j += 1
        return res if res != float('inf') else 0
