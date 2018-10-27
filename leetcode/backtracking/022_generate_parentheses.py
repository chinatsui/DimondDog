class Solution:
    def generate_parentheses(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left = right = n
        res = []
        self._backtrack('',res, left, right)
        return res

    def _backtrack(self, cur, res, left, right):
        if left == 0 and right == 0:
            res.append(cur)
            return
        if left > 0:
            self._backtrack(cur + '(', res, left - 1, right)
        if right > left:
            self._backtrack(cur + ')', res, left, right - 1)


print(Solution().generate_parentheses(5))
