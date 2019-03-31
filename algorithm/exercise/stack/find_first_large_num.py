"""
Given an array of integers arr1, return an array arr2 in which arr2[i] happens to be the first num larger than arr1[i].
Example:
Input: [1, 3, -4, 6, 5]
Output: [3, 6, 6, 6, 5]
"""


class Solution:

    @staticmethod
    def find_first_larger_nums(nums):
        if not nums:
            return nums

        res = [0] * len(nums)
        stack = []
        for (i, num) in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                k = stack.pop()
                res[k] = num
            stack.append(i)

        while stack:
            k = stack.pop()
            res[k] = nums[k]

        return res


print(Solution().find_first_larger_nums([1, 3, -4, 6, 5]))
