"""
Given a positive integer N, return the number of positive integers
less than or equal to N that have at least 1 repeated digit.

Example 1:
Input: 20
Output: 1
Explanation:
The only positive number (<= 20) with at least 1 repeated digit is 11.

Example 2:
Input: 100
Output: 10
Explanation:
The positive numbers (<= 100) with at least 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.

Example 3:
Input: 1000
Output: 262

Note:
1 <= N <= 10^9
"""


class Solution:
    @staticmethod
    def num_dup_digits_at_most_N(N):
        L = list(map(int, str(N + 1)))
        res, n = 0, len(L)

        def permutation(p, d):
            return 1 if d == 0 else (p - d + 1) * permutation(p, d - 1)

        # count non-repeated numbers of *, **, *** ... *{n-1}
        for i in range(1, n):
            res += 9 * permutation(9, i - 1)

        # If N = 72345, then we additionally count non-repeat numbers in below ranges:
        # 10000...69999
        # 70000...71999
        # 72000...72299
        # 72300...72339
        # 72340...72345
        s = set()
        for i, x in enumerate(L):
            # leading digit cannot be zero
            for y in range(0 if i else 1, x):
                # e.g. When i reaches 2, we have options of 0...2 for this digit,
                # however 7, 2 already exists in set, we skip processing 2 as 722** has repeated numbers.
                if y not in s:
                    res += permutation(9 - i, n - i - 1)
            if x in s:
                break
            s.add(x)
        return N - res


print(Solution().num_dup_digits_at_most_N(72345))
