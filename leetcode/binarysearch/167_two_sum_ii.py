class Solution:
    @staticmethod
    def two_sum(numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo, hi = 0, len(numbers) - 1
        sum = numbers[lo] + numbers[hi]
        while lo < hi:
            if sum == target:
                return [lo + 1, hi + 1]
            elif sum < target:
                lo += 1
            else:
                hi -= 1
            sum = numbers[lo] + numbers[hi]
