"""
LeetCode-130

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:
X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X

Explanation:
Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
from collections import deque


class BFSSolution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        def adjacent(i, j):
            for (x, y) in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                if 0 <= x < m and 0 <= y < n:
                    yield (x, y)

        m, n = len(board), len(board[0])
        visited = set()
        trace = set()

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and board[i][j] == 'O':
                    q = deque()
                    surrounded = True

                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        surrounded = False

                    q.append((i, j))
                    visited.add((i, j))
                    trace.add((i, j))

                    while q:
                        x, y = q.popleft()
                        board[x][y] = 'X'
                        for cor in adjacent(x, y):
                            nx = cor[0]
                            ny = cor[1]
                            if cor not in visited and board[nx][ny] == 'O':
                                if nx == 0 or nx == m - 1 or ny == 0 or ny == n - 1:
                                    surrounded = False
                                q.append(cor)
                                visited.add(cor)
                                trace.add(cor)

                    if not surrounded:
                        for (x, y) in trace:
                            board[x][y] = 'O'

                    trace.clear()


class DFSSolution:
    def solve(self, board):
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and board[i][j] == 'O':
                    if (i == 0 or i == m - 1 or n == 0 or n == n - 1):
                        self._dfs(board, i, j, visited, 'U')
                    else:
                        self._dfs(board, i, j, visited, 'X')

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'U':
                    board[i][j] = 'O'

    def _dfs(self, board, x, y, visited, mark):
        board[x][y] = mark
        visited.add((x, y))

        for (nx, ny) in self.adjacent(board, x, y):
            if (nx, ny) not in visited and board[nx][ny] == 'O':
                self._dfs(board, nx, ny, visited, mark)

    @staticmethod
    def adjacent(board, i, j):
        for (x, y) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= x < len(board) and 0 <= y < len(board[0]):
                yield (x, y)


t_board = [
    ["O", "X", "O", "O", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "X", "O", "O", "O", "O", "X"],
    ["O", "X", "O", "X", "O", "O", "O", "O", "X"],
    ["O", "O", "O", "O", "X", "O", "O", "O", "O"],
    ["X", "O", "O", "O", "O", "O", "O", "O", "X"],
    ["X", "X", "O", "O", "X", "O", "X", "O", "X"],
    ["O", "O", "O", "X", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "X", "O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O", "X", "X", "O", "O"]]

DFSSolution().solve(t_board)
print(t_board)
