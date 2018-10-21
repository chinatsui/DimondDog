class Solution:
    def sqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        lo, hi = 0, x
        while lo < hi:
            mid = (lo + hi) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                lo = mid + 1
            else:
                hi = mid
        return lo if lo ** 2 == x else lo - 1
