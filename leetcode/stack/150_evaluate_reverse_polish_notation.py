class Solution:
    @staticmethod
    def eval_rpn(tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = {'+', '-', '*', '/'}
        stack = []
        for x in tokens:
            if x in operators:
                num1 = stack.pop()
                num2 = stack.pop()
                if x == '+':
                    stack.append(num2 + num1)
                elif x == '-':
                    stack.append(num2 - num1)
                elif x == '*':
                    stack.append(num2 * num1)
                else:
                    negative = True if num2 // num1 < 0 else False
                    num2 = abs(num2)
                    num1 = abs(num1)
                    divide_res = num2 // num1
                    stack.append(divide_res if not negative else -divide_res)

            else:
                stack.append(int(x))
        return stack.pop()


print(Solution().eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
