"""
LeetCode-74

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""


class Solution:
    def search_matrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])

        for i in range(0, m - 1):
            if matrix[i][0] <= target < matrix[i + 1][0]:
                return self._binary_search(matrix[i], target)

        return self._binary_search(matrix[m - 1], target)

    @staticmethod
    def _binary_search(nums, target):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if nums[mi] == target:
                return True
            elif nums[mi] < target:
                lo = mi + 1
            else:
                hi = mi
        return True if nums[lo] == target else False


print(Solution().search_matrix([[1, 3]], 3))
