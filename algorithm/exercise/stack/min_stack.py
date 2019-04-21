"""
LeetCode-155

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        cur_min = self.get_min()
        cur_min = x if not cur_min else min(cur_min, x)
        self.data.append((x, cur_min))

    def pop(self):
        """
        :rtype: void
        """
        self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1][0]

    def get_min(self):
        """
        :rtype: int
        """
        if self.data:
            return self.data[-1][1]
        else:
            return None


class MinStack2:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = None

    def push(self, x: int) -> None:
        if not self.data:
            self.min = x
        elif x <= self.min:
            self.data.append(self.min)
            self.min = x
        self.data.append(x)

    def pop(self) -> None:
        if self.data:
            if self.min == self.data.pop():
                self.min = self.data.pop() if self.data else None

    def top(self) -> int:
        return self.data[-1] if self.data else None

    def get_min(self) -> int:
        return self.min
