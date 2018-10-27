class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []

        nums2 = sorted(nums2)
        res = []
        while nums1 and nums2:
            n = nums1.pop(0)
            idx = self._binary_search(n, nums2)
            if idx != -1:
                res.append(n)
                nums2.pop(idx)
        return res

    @staticmethod
    def _binary_search(n, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == n:
                return mid
            elif nums[mid] < n:
                lo = mid + 1
            else:
                hi = mid
        return lo if nums[lo] == n else -1


print(Solution().intersect([1, 2, 2, 1], [2, 2]))
