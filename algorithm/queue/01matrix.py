"""
LeetCode-542

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:
Input:
0 0 0
0 1 0
0 0 0

Output:
0 0 0
0 1 0
0 0 0

Example 2:
Input:
0 0 0
0 1 0
1 1 1

Output:
0 0 0
0 1 0
1 2 1

Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""


class Solution:
    @staticmethod
    def update_matrix(matrix):
        m, n = len(matrix), len(matrix[0])

        def adjacent(i, j):
            for (x, y) in ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)):
                if 0 <= x < m and 0 <= y < n:
                    yield (x, y)

        q = []
        visited = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append((i, j, 0))
                    visited.add((i, j))

        res = [[0] * n for _ in range(m)]

        while q:
            (i, j, distance) = q.pop(0)
            res[i][j] = distance
            for (x, y) in adjacent(i, j):
                if (x, y) not in visited:
                    visited.add((x, y))
                    q.append((x, y, distance + 1))
        return res


print(Solution().update_matrix([[1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
                                [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
                                [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                                [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
                                [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
                                [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                                [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
                                [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
                                [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                                [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]))
