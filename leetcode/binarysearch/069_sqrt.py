class Solution:
    @staticmethod
    def sqrt(x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2

            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                right = mid - 1
            else:
                left = mid + 1

            if left > right:
                return right
