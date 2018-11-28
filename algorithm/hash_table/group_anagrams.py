"""
LeetCode-49

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

"""


class Solution:
    @staticmethod
    def group_anagrams(strs):
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
