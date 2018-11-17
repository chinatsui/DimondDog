class Solution:

    def generate(self, n):
        res = []
        self._backtrack(n, n, '', res)
        return res

    def _backtrack(self, left, right, cur, res):
        if left == 0 and right == 0:
            res.append(cur)
            return

        if left > 0:
            self._backtrack(left - 1, right, cur + '(', res)

        if right > left:
            self._backtrack(left, right - 1, cur + ')', res)


print(Solution().generate(3))
