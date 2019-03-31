"""
Given a number 'num', find another two numbers 'a' and 'b' to make pow(a,2) + pow(b,2) = num, then return [a,b]
If there doesn't exist such a pair of numbers, return an empty array.

Example 1:
Input: 58.
Output: [3, 7]
Explanation: 3^2 + 7^2 = 58

Example 2:
Input: 12.
Output: []
Explanation: There doesn't exist a pair of numbers to make pow(a,2) + pow(b,2) == 12
"""


class Solution:

    def find_two_square_nums(self, num):
        if num < 0:
            return []

        max_sqrt = self._max_sqrt(num)
        i, j = 0, max_sqrt
        while i <= j:
            sum = pow(i, 2) + pow(j, 2)
            if sum == num:
                return [i, j]
            elif sum < num:
                i += 1
            else:
                j -= 1
        return []

    @staticmethod
    def _max_sqrt(n):
        i = 0
        while pow(i, 2) <= n:
            i += 1
        return i - 1


print(Solution().find_two_square_nums(12))
