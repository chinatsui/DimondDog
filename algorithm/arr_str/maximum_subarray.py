"""
LeetCode-53

Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6

Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution:

    @staticmethod
    def max_sub_array(nums):
        if not nums:
            return None

        tmp = (0, 0, nums[0])
        res = tmp

        for (i, n) in enumerate(nums):
            if tmp[2] + n > n:
                tmp = (tmp[0], i, tmp[2] + n)
            else:
                tmp = (i, i, n)

            if res[2] < tmp[2]:
                res = tmp

        return res


print(Solution().max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
