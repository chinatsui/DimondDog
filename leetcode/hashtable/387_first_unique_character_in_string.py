class Solution:
    def first_uniq_char(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1

        ch_count_map = dict()
        for (idx, ch) in enumerate(s):
            if ch in ch_count_map:
                (idx, count) = ch_count_map[ch]
                count += 1
                ch_count_map[ch] = (idx, count)
            else:
                ch_count_map[ch] = (idx, 1)

        idx_list = []
        for (ch, (idx, count)) in ch_count_map.items():
            if count == 1:
                idx_list.append(idx)

        return min(idx_list) if idx_list else -1
