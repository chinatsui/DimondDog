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
