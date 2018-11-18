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
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return False

        if not board or not board[0]:
            return False

        visited = [[False] * len(row) for row in board]

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if self._backtrack(board, i, j, word, 0, visited):
                    return True
        return False

    def _backtrack(self, board, i, j, word, idx, visited):
        if idx == len(word):
            return True

        if i < 0 or j < 0 or i == len(board) or j == len(board[0]) or visited[i][j]:
            return False

        if board[i][j] != word[idx]:
            return False

        visited[i][j] = True
        exists = self._backtrack(board, i - 1, j, word, idx + 1, visited) \
                 or self._backtrack(board, i + 1, j, word, idx + 1, visited) \
                 or self._backtrack(board, i, j - 1, word, idx + 1, visited) \
                 or self._backtrack(board, i, j + 1, word, idx + 1, visited)
        visited[i][j] = False
        return exists


t_board = [
    ['a', 'a']
]
print(Solution().exist(t_board, 'aaa'))
