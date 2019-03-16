"""
LeetCode-6

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"

Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
"""


class Solution:
    """
    A very good problem can help think of how to write loops in the nested or parallel layout.
    """

    @staticmethod
    def convert(s, numRows):
        if numRows <= 1:
            return s

        strList = [[] for _ in range(numRows)]

        i = 0
        while i < len(s):
            for j in range(numRows):
                if i >= len(s):
                    break;
                strList[j].append(s[i])
                i += 1
            for k in range(numRows - 2, 0, -1):
                if i >= len(s):
                    break;
                strList[k].append(s[i])
                i += 1

        res = ''
        for i in range(numRows):
            tmp = ''.join(strList[i])
            res = ''.join([res, tmp])

        return res


print(Solution().convert("PAYPALISHIRING", 3))
