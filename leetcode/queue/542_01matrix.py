class Solution:
    @staticmethod
    def update_matrix(matrix):
        m, n = len(matrix), len(matrix[0])

        def adjacent(i, j):
            for (x, y) in ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)):
                if 0 <= x < m and 0 <= y < n:
                    yield (x, y)

        q = [((i, j), 0) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        visited = set([cor for cor, _ in q])
        res = [[0] * n for _ in range(m)]
        while q:
            (i, j), distance = q.pop(0)
            res[i][j] = distance
            for adj in adjacent(i, j):
                if adj not in visited:
                    visited.add(adj)
                    q.append((adj, distance + 1))
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
