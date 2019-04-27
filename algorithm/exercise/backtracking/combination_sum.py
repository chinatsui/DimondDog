"""
LeetCode-39

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution:
    def combinationSum(self, candidates, target):
        res, candidates = [], sorted(candidates)
        self.backtrack(candidates, target, res, [], 0)
        return res

    def backtrack(self, candidates, target, res, cur, i):
        if sum(cur) == target:
            res.append(cur)
        elif sum(cur) > target:
            return
        else:
            for k in range(i, len(candidates)):
                if candidates[k] > target:
                    break
                self.backtrack(candidates, target, res, cur + [candidates[k]], k)
