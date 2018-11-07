class Solution:
    @staticmethod
    def find_restaurant(list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res = []
        idx_sum = -1
        name_idx_map1 = {name: idx for (idx, name) in enumerate(list1)}
        for (i, n) in enumerate(list2):
            if n in name_idx_map1:
                cur_idx_sum = i + name_idx_map1[n]
                if idx_sum == -1:
                    idx_sum = cur_idx_sum
                    res.append(n)
                elif idx_sum == cur_idx_sum:
                    res.append(n)
                elif idx_sum > cur_idx_sum:
                    idx_sum = cur_idx_sum
                    res.clear()
                    res.append(n)
        return res
