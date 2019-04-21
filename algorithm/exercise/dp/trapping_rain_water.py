"""
LeetCode-42

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


class Solution:

    @staticmethod
    def trap(height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        left, left_wall, right, right_wall = 0, 0, len(height) - 1, 0
        water = 0

        while left < right:
            left_wall = max(left_wall, height[left])
            right_wall = max(right_wall, height[right])
            if left_wall > right_wall:
                water += right_wall - height[right]
                right -= 1
            else:
                water += left_wall - height[left]
                left += 1

        return water


class Solution2:

    @staticmethod
    def trap(height) -> int:
        if not height:
            return 0

        lo, hi = 0, len(height) - 1
        lo_wall, right_wall = height[lo], height[hi]
        water = 0
        while lo < hi:
            if height[lo] < height[hi]:
                water += max(0, min(lo_wall, right_wall) - height[lo])
                lo += 1
                lo_wall = max(lo_wall, height[lo])
            else:
                water += max(0, min(lo_wall, right_wall) - height[hi])
                hi -= 1
                right_wall = max(right_wall, height[hi])

        return water
