class Solution:

    def __init__(self, size):
        self.size = size

    def place_queens(self):
        res = []
        for col in range(self.size):
            self._place(0, col, {}, res)
        return res

    def _place(self, row, col, rc_map, res):
        if self._check(row, col, rc_map):
            rc_map[row] = col
            if row == self.size - 1:
                res.append([entry for entry in rc_map.items()])
                return

            for nxt in range(self.size):
                if nxt == col:
                    continue
                self._place(row + 1, nxt, rc_map, res)

    @staticmethod
    def _check(row, col, row_col_map):
        for r in range(row):
            if row_col_map[r] == col:  # check column
                return False

            if abs(r - row) == abs(row_col_map[r] - col):  # check diagonal line
                return False
        return True


t_res = Solution(8).place_queens()
print(f'total: {len(t_res)}')
for ans in t_res:
    print(ans)
