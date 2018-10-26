import bisect


class Solution:
    @staticmethod
    def find_closest_elements(arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if not arr:
            return []

        left = right = bisect.bisect_left(arr, x)
        while right - left < k:
            if left == 0:
                return arr[:k]

            if right == len(arr):
                return arr[-k:]

            if abs(arr[left - 1] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1

        return arr[left:right]


print(Solution().findClosestElements([1, 2, 3, 5, 6], 4, 4))
