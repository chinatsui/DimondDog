"""
LeetCode - 169
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
"""


class Solution:
    @staticmethod
    def majority_element(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        i, cnt, res = 0, 0, nums[0]
        for j in range(len(nums) - 1):
            if nums[j] != nums[j + 1]:
                diff = j - i + 1
                if diff > cnt:
                    cnt = diff
                    res = nums[i]
                i = j + 1

        # After loop completes, we need to take i...len(nums) - 1 for consideration
        if len(nums) - i > cnt:
            res = nums[i]

        return res
