"""
LeetCode-454

Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l)
there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500.
All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""
from collections import Counter


class Solution:
    """
    Bi-loop for a in A, b in B to calculate (a + b) and put it into hash map.
    Then bi-loop c in C, d in D to calculate (-c - d) and search it in previous hash map.
    """
    @staticmethod
    def four_sum_count(A, B, C, D):
        ab_count = Counter([a + b for a in A for b in B])
        return sum([ab_count[-c - d] for c in C for d in D])


print(Solution().four_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2]))
