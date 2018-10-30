class Solution:
    @staticmethod
    def num_islands(grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        visited = [[False] * len(row) for row in grid]
        m = len(grid)
        n = len(grid[0])

        count = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    q = [(i, j)]
                    while q:
                        item = q.pop(0)
                        x = item[0]
                        y = item[1]
                        if x < 0 or x == len(grid) or y < 0 or y == len(grid[0]) or visited[x][y] or grid[x][y] == '0':
                            continue
                        grid[x][y] = '0'
                        visited[x][y] = True
                        q.append((x + 1, y))
                        q.append((x - 1, y))
                        q.append((x, y + 1))
                        q.append((x, y - 1))
        return count
