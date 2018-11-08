class Solution:
    def is_valid_sudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_map = dict()
        col_map = dict()
        squ_map = dict()

        for i in range(0, 9):
            for j in range(0, 9):
                cur = board[i][j]

                if '.' == cur:
                    continue

                if not self._partial_check(row_map, i, cur):
                    return False

                if not self._partial_check(col_map, j, cur):
                    return False

                if not self._partial_check(squ_map, self._convert_to_squ_key(i, j), cur):
                    return False
        return True

    @staticmethod
    def _partial_check(map, key, num):
        if key in map:
            if num in map[key]:
                return False
            else:
                map[key].add(num)
        else:
            map[key] = set([num])
        return True

    @staticmethod
    def _convert_to_squ_key(i, j):
        if i in range(0, 3):
            if j in range(0, 3):
                return 0
            elif j in range(3, 6):
                return 1
            else:
                return 2
        elif i in range(3, 6):
            if j in range(0, 3):
                return 3
            elif j in range(3, 6):
                return 4
            else:
                return 5
        else:
            if j in range(0, 3):
                return 6
            elif j in range(3, 6):
                return 7
            else:
                return 8


print(Solution().is_valid_sudoku(
    [["5", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."],
     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
