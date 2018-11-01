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
