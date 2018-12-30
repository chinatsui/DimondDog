"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""


class Solution:
    """
    Use two pointers to address the issue, I just made it at the first time.
    """

    @staticmethod
    def max_area(height):
        left, right = 0, len(height) - 1

        max_water = 0
        while left < right:
            cur_water = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, cur_water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
