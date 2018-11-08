class Solution:
    @staticmethod
    def group_anagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []

        mapping = dict()
        for s in strs:
            key = ''.join(sorted(s))
            if key in mapping:
                mapping[key].append(s)
            else:
                mapping[key] = [s]
        return [str_list for (key, str_list) in mapping.items()]
