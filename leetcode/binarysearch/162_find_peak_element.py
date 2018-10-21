class Solution:
    @staticmethod
    def find_peak_element(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        lo, hi = 0, len(nums) - 1
        while lo + 1 < hi: # at least 3 elements
            mid = (lo + hi) // 2

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                # mid is in left slope, peak is on the right of mid
                lo = mid + 1
            else:
                hi = mid
        if lo == hi:
            return lo
        else:
            return lo if nums[lo] > nums[hi] else hi
