class Solution:
    @staticmethod
    def is_happy(n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n > 1:
            nxt = 0
            for d in str(n):
                nxt += int(d) ** 2

            if nxt == 1:
                return True
            elif nxt in seen:
                return False
            else:
                seen.add(nxt)
                n = nxt
        return True
