"""
LeetCode-81

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Follow up:
This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
"""


class Solution(object):
    @staticmethod
    def search(nums, target):
        if not nums:
            return False

        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mi = lo + (hi - lo) // 2

            if nums[mi] == target:
                return True

            if nums[mi] < nums[hi]:
                if nums[mi] < target <= nums[hi]:
                    lo = mi + 1
                else:
                    hi = mi - 1
            elif nums[mi] > nums[hi]:
                if nums[lo] <= target < nums[mi]:
                    hi = mi - 1
                else:
                    lo = mi + 1
            else:
                hi -= 1

        return True if nums[lo] == target else False
