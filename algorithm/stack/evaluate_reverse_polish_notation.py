"""
LeetCode-150

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid.
That means the expression would always evaluate to a result and there won't be any divide by zero operation.

Example 1:
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""


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
