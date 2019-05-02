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


class Solution2(object):
    def find_closest_elements(self, arr, k, x):
        if not arr:
            return []

        left = right = self._find_num(arr, x)
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

    @staticmethod
    def _find_num(arr, target):
        lo, hi = 0, len(arr) - 1

        while lo < hi:
            mi = lo + (hi - lo) // 2
            if arr[mi] == target:
                return mi
            elif arr[mi] < target:
                lo = mi + 1
            else:
                hi = mi

        if arr[lo] == target:
            return lo
        elif arr[lo] < target:
            return lo + 1
        else:
            return lo
