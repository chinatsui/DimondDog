"""
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
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        row_pos = self._binary_search_first_column(matrix, target)

        if row_pos < 0:
            return False

        if matrix[row_pos][0] == target:
            return True

        return self._binary_search_matrix_row(matrix, row_pos, target)

    @staticmethod
    def _binary_search_matrix_row(matrix, row, target):
        lo, hi = 0, len(matrix[0]) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            mid_num = matrix[row][mid]
            if mid_num == target:
                return True
            elif mid_num < target:
                lo = mid + 1
            else:
                hi = mid
        return matrix[row][lo] == target

    @staticmethod
    def _binary_search_first_column(matrix, target):
        lo, hi = 0, len(matrix) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if matrix[mid][0] == target:
                return mid
            elif matrix[mid][0] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo if matrix[lo][0] <= target else lo - 1


print(Solution().searchMatrix([[1, 3]], 3))
