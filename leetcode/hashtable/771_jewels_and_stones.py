class Solution:
    @staticmethod
    def num_jewels_in_stones(J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = set(J)
        count = 0
        for ch in S:
            if ch in jewels:
                count += 1
        return count
