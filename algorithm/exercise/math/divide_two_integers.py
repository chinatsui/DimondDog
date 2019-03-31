class Solution:

    @staticmethod
    def divide(dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        if dividend < divisor:
            return 0

        res = 0
        while dividend >= divisor:
            i = 1
            tmp = divisor
            while dividend >= tmp:
                res += i
                dividend -= tmp
                i <<= 2
                tmp <<= 2

        if not positive:
            res = -res

        return res


print(Solution().divide(12, -2))
print(Solution().divide(-12, 2))
print(Solution().divide(-12, -2))
print(Solution().divide(1, 1))
print(Solution().divide(3, 3))
