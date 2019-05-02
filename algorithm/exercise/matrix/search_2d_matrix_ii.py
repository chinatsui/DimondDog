"""
LeetCode-240

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example:
Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.
Given target = 20, return false.
"""


class Solution:
    """
    Start from top right corner position, if cur < target: i++, else: j--
    """

    @staticmethod
    def search_matrix(matrix, target):
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1

        while x < m and y >= 0:
            cur = matrix[x][y]
            if cur == target:
                return True
            elif cur < target:
                x += 1
            else:
                y -= 1

        return False
