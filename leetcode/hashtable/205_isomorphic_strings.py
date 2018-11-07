class Solution:
    def is_isomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        return self._transform(s) == self._transform(t)

    @staticmethod
    def _transform(var):
        res = ''
        ch_map = dict()
        mark = 0
        for ch in var:
            if ch in ch_map:
                res += ch_map[ch]
            else:
                ch_map[ch] = str(mark)
                mark += 1
        return res
