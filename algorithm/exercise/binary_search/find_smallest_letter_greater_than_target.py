"""
LeetCode-744

Given a list of sorted characters letters containing only lowercase letters, and given a target letter target,
find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"

Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
"""


class Solution:
    @staticmethod
    def next_greatest_letter(letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target < letters[0]:
            return letters[0]

        if target > letters[-1]:
            return letters[0]

        lo, hi = 0, len(letters) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if letters[mid] == target:
                while mid + 1 < len(letters) and letters[mid + 1] == letters[mid]:
                    mid += 1
                if mid + 1 < len(letters):
                    return letters[mid + 1]
                else:
                    return letters[0]
            elif letters[mid] < target:
                lo = mid + 1
            else:
                hi = mid

        #  If we didn't find the target in above while loop, then just make sure if lo is the last index and compare
        #  nums[lo] and target to see if the position of insertion is "lo" or "lo + 1".
        #  When letters[lo] < target, then position is lo + 1,
        #  so return letters[0] according to the problem requirements. Otherwise returns letters[lo]
        if lo == len(letters) - 1 and letters[lo] <= target:
            return letters[0]

        return letters[lo]
