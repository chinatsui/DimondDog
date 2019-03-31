"""
LeetCode-658

Given a sorted array, two integers k and x, find the k closest elements to x in the array.
The result should also be sorted in ascending order.
If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]

Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]

Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104
"""
import bisect


class Solution:
    @staticmethod
    def find_closest_elements(arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if not arr:
            return []

        left = right = bisect.bisect_left(arr, x)
        while right - left < k:
            if left == 0:
                return arr[:k]

            if right == len(arr):
                return arr[-k:]

            if abs(arr[left - 1] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1

        return arr[left:right]


print(Solution().find_closest_elements([1, 2, 3, 5, 6], 4, 4))
