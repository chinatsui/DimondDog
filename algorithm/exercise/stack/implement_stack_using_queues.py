"""
LeetCode-225

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.

Example:
MyStack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false

Notes:
You must use only standard operations of a queue --
which means only push to back, peek/pop from front, size, and is empty operations are valid.

Depending on your language, queue may not be supported natively.
You may simulate a queue by using a list or deque (double-ended queue),
as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""

from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if not self.q1:
            self.q2.append(x)
        else:
            self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.q1:
            while len(self.q1) > 1:
                self.q2.append(self.q1.popleft())
            return self.q1.popleft()
        else:
            while len(self.q2) > 1:
                self.q1.append(self.q2.popleft())
            return self.q2.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[-1] if self.q1 else self.q2[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q1 and not self.q2
