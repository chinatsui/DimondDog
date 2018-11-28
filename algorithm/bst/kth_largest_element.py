"""
LeetCode-703

Design a class to find the kth largest element in a stream.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums,
which contains initial elements from the stream.
For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:
int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8

Note:
You may assume that nums' length ≥ k-1 and k ≥ 1.
"""

import heapq


class Solution1(object):
    class BSTNode(object):
        def __init__(self, val):
            self.val = val
            self.cnt = 1
            self.left = None
            self.right = None

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.root = None
        for n in nums:
            self.root = self._insert_bst(self.root, n)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.root = self._insert_bst(self.root, val)
        return self._find_kth(self.k)

    def _insert_bst(self, root, n):
        if not root:
            return self.BSTNode(n)
        root.cnt += 1
        if n < root.val:
            root.left = self._insert_bst(root.left, n)
        else:
            root.right = self._insert_bst(root.right, n)
        return root

    def _find_kth(self, k):
        cur = self.root
        while k > 0:
            r_cnt = 1 + cur.right.cnt if cur.right else 1
            if k == r_cnt:
                break
            elif k < r_cnt:
                cur = cur.right
            else:
                k -= r_cnt
                cur = cur.left
        return cur.val


class Solution2:
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif self.nums[0] < val:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]


solution = Solution2(3, [4, 5, 8, 2]);
print(solution.add(3))
print(solution.add(5))
print(solution.add(10))
print(solution.add(9))
print(solution.add(4))
