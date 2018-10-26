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

        if lo == len(letters) - 1:
            if letters[lo] <= target:
                return letters[0]
            else:
                return letters[lo]

        return letters[lo]
