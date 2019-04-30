"""
LeetCode-12

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together.
Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution:
    @staticmethod
    def int_to_roman(num):
        if num < 1 or num > 3999:
            return None

        def convert(lo, mi, hi, di):
            if 1 <= di <= 3:
                return lo * di
            elif di == 4:
                return lo + mi
            elif di == 5:
                return mi
            elif 6 <= di <= 8:
                return mi + lo * (di - 5)
            else:
                return lo + hi

        res, i = '', 1
        while num:
            di = num % 10

            if di != 0:
                if i == 1:
                    res = convert('I', 'V', 'X', di) + res
                elif i == 10:
                    res = convert('X', 'L', 'C', di) + res
                elif i == 100:
                    res = convert('C', 'D', 'M', di) + res
                elif i == 1000:
                    res = 'M' * di + res
            i *= 10
            num = num // 10

        return res


print(Solution().int_to_roman(10))
