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
What if elements of nums2 are stored on disk, and the memory is limited such that
you cannot load all elements into the memory at once?
"""


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []

        num_count_map1 = self._reduce(nums1)
        num_count_map2 = self._reduce(nums2)

        res = []
        for (num, count) in num_count_map1.items():
            if num in num_count_map2:
                for _ in range(min(count, num_count_map2[num])):
                    res.append(num)
        return res

    @staticmethod
    def _reduce(nums):
        mapping = dict()
        for n in nums:
            if n in mapping:
                mapping[n] += 1
            else:
                mapping[n] = 1
        return mapping
