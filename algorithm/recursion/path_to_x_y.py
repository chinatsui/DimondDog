"""
CC150-9.2
"""

class Solution:

    def get_path(self, matrix):
        cache = {}
        path = []
        self._traverse(0, 0, matrix, path, cache)
        return path

    def _traverse(self, x, y, matrix, path, cache):
        """
        During DFS, we might visit a node more than once,
        use a cache to store it to directly get the answer for next time,
        this is a sort of DP.
        """
        if (x, y) in cache:
            return cache[(x, y)]

        path.append((x, y))
        if x == len(matrix[0]) - 1 and y == len(matrix) - 1:
            return True

        success = False
        if x + 1 < len(matrix[0]) and matrix[x + 1][y]:
            success = self._traverse(x + 1, y, matrix, path, cache)

        if not success and y + 1 < len(matrix) and matrix[x][y + 1]:
            success = self._traverse(x, y + 1, matrix, path, cache)

        if not success:
            path.pop()

        cache[(x, y)] = success

        return success


t_matrix = [[True] * 10 for _ in range(10)]
t_matrix[4][5] = False
t_matrix[9][3] = False
t_matrix[7][8] = False
print(Solution().get_path(t_matrix))
