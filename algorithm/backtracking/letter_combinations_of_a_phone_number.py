"""
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""


class Solution:
    @staticmethod
    def letter_combinations(digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        num_map = {}
        num_map['2'] = 'abc'
        num_map['3'] = 'def'
        num_map['4'] = 'ghi'
        num_map['5'] = 'jkl'
        num_map['6'] = 'mno'
        num_map['7'] = 'pqrs'
        num_map['8'] = 'tuv'
        num_map['9'] = 'wxyz'

        res = []
        for num in digits:
            if '2' <= num <= '9':
                chars = num_map[num]

                if not res:
                    for ch in chars:
                        res.append(ch)
                    continue

                tmp = []
                for cur in res:
                    for ch in chars:
                        tmp.append(cur + ch)
                res = tmp
        return list(res)


print(Solution().letter_combinations('23'))
