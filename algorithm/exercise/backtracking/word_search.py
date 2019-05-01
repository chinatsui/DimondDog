"""
LeetCode-79

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


class Solution:

    def exist(self, board, word):
        if not word:
            return False

        if not board or not board[0]:
            return False

        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        for x in range(m):
            for y in range(n):
                if self._backtrack(board, word, visited, x, y, 0):
                    return True
        return False

    def _backtrack(self, board, word, visited, x, y, i):
        if x < 0 or x == len(board) or y < 0 or y == len(board[0]) or visited[x][y]:
            return False

        if board[x][y] != word[i]:
            return False

        if i == len(word) - 1:
            return True

        visited[x][y] = True
        exists = self._backtrack(board, word, visited, x + 1, y, i + 1) \
                 or self._backtrack(board, word, visited, x - 1, y, i + 1) \
                 or self._backtrack(board, word, visited, x, y + 1, i + 1) \
                 or self._backtrack(board, word, visited, x, y - 1, i + 1)
        visited[x][y] = False
        return exists


t_board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]
print(Solution().exist(t_board, 'EESECBASADFC'))
