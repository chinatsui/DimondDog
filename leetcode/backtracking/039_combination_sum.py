class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self._backtrack([], res, candidates, 0, target)
        return res

    def _backtrack(self, cur, res, candidates, start, target):
        if sum(cur) == target:
            res.append(cur)
            return

        if sum(cur) > target:
            return

        for i in range(start, len(candidates)):
            self._backtrack(cur + [candidates[i]], res, candidates, i, target)
