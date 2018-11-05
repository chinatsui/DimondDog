class Solution:

    @staticmethod
    def updateMatrix(matrix):
        m, n = len(matrix), len(matrix[0])

        def neighbors(i, j):
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n:
                    yield x, y

        q = [((i, j), 0) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        visited = {(i, j) for (i, j), _ in q}
        res = [[0] * n for _ in matrix]
        while q:
            (i, j), distance = q.pop(0)
            res[i][j] = distance
            for nei in neighbors(i, j):
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, distance + 1))

        return res


print(Solution().updateMatrix([[1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
                               [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
                               [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                               [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
                               [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
                               [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                               [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
                               [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
                               [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                               [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]))
