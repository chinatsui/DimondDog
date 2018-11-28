"""
LeetCode-350
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""


class Solution:
    """
    In addition to BinarySearch, two pointers are also a good approach for a sorted array.
    """

    def intersect(self, nums1, nums2):
        """
        TODO: The implementation of this problem is not good, use hashMap or two pointers(sort nums1, nums2) instead.
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
