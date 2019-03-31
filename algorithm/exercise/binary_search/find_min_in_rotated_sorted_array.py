"""
LeetCode-153

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:
Input: [3,4,5,1,2]
Output: 1

Example 2:
Input: [4,5,6,7,0,1,2]
Output: 0
"""


class Solution:
    @staticmethod
    def find_min(nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        return nums[lo]


print(Solution().find_min([3, 0, 1]))
print(Solution().find_min([4, 5, 6, 7, 0, 1, 2]))
print(Solution().find_min([3, 4, 5, 1, 2]))
