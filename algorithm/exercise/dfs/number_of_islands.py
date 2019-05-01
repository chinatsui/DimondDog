"""
LeetCode-200

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
"""


class Solution:

    def num_islands(self, grid):
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    cnt += 1
                    self._dfs(grid, i, j)
        return cnt

    def _dfs(self, grid, x, y):
        if x < 0 or x == len(grid) or y < 0 or y == len(grid[0]) or grid[x][y] == '0':
            return

        grid[x][y] = '0'

        self._dfs(grid, x + 1, y)
        self._dfs(grid, x - 1, y)
        self._dfs(grid, x, y + 1)
        self._dfs(grid, x, y - 1)


print(Solution().num_islands(
    [["1", "1", "1", "1", "0"],
     ["1", "1", "0", "1", "0"],
     ["1", "1", "0", "0", "0"],
     ["0", "0", "0", "0", "0"]]))
