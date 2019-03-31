"""
LeetCode-20

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""


class Solution:
    @staticmethod
    def is_valid(s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        stack = list(s)
        right_brackets = []
        while stack:
            cur = stack.pop()
            if cur == '}' or cur == ')' or cur == ']':
                right_brackets.append(cur)
            else:
                if not right_brackets:
                    return False
                else:
                    cur_right = right_brackets.pop()
                    if cur == '[' and cur_right == ']':
                        continue
                    elif cur == '{' and cur_right == '}':
                        continue
                    elif cur == '(' and cur_right == ')':
                        continue
                    else:
                        return False
        return True if not stack and not right_brackets else False
