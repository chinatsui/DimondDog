from collections import Counter


class Solution:
    @staticmethod
    def four_sum_count(A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ab_count = Counter([a + b for a in A for b in B])
        return sum([ab_count[-c - d] for c in C for d in D])


print(Solution().four_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2]))
