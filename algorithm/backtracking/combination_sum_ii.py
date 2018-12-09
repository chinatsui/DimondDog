"""
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []

        res = []
        candidates = sorted(candidates)
        self.backtrack(candidates, target, 0, [], res)
        return res

    def backtrack(self, candidates, target, i, cur, res):
        if target == 0:
            res.append(cur)
        elif target < 0:
            return
        else:
            n = len(candidates)
            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                val = candidates[j]
                self.backtrack(candidates, target - val, j + 1, cur + [val], res)
