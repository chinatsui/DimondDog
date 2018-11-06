class Solution:
    @staticmethod
    def num_islands(grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])

        count = 0
        visited = set()

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    count += 1
                    q = [(i, j)]
                    while q:
                        (x, y) = q.pop(0)

                        if x < 0 or x == m or y < 0 or y == n:
                            continue

                        if (x, y) in visited:
                            continue

                        if grid[x][y] == '0':
                            continue

                        grid[x][y] = '0'

                        visited.add((x, y))
                        q.append((x + 1, y))
                        q.append((x - 1, y))
                        q.append((x, y + 1))
                        q.append((x, y - 1))
        return count


print(Solution().num_islands(
    [["1", "1", "1", "1", "0"],
     ["1", "1", "0", "1", "0"],
     ["1", "1", "0", "0", "0"],
     ["0", "0", "0", "0", "0"]]))
