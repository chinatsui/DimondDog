class Solution:
    def flood_fill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        visited = [[False] * len(row) for row in image]
        self._dfs(image, sr, sc, visited, image[sr][sc], newColor)
        return image

    def _dfs(self, image, i, j, visited, start_pixel_color, new_color):
        if i < 0 or i == len(image) or j < 0 or j == len(image[0]) or visited[i][j] or image[i][j] != start_pixel_color:
            return

        image[i][j] = new_color
        visited[i][j] = True
        self._dfs(image, i + 1, j, visited, start_pixel_color, new_color)
        self._dfs(image, i - 1, j, visited, start_pixel_color, new_color)
        self._dfs(image, i, j + 1, visited, start_pixel_color, new_color)
        self._dfs(image, i, j - 1, visited, start_pixel_color, new_color)


print(Solution().flood_fill([[0, 0, 0], [0, 0, 0]], 0, 0, 2))
