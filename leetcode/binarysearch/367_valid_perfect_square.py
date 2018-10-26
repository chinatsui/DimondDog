class Solution:
    @staticmethod
    def is_perfect_square(num):
        """
        :type num: int
        :rtype: bool
        """
        lo, hi = 0, num
        while lo < hi:
            mid = (lo + hi) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                lo = mid + 1
            else:
                hi = mid
        return True if lo ** 2 == num else False
