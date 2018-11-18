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

You must use only standard operations of a queue -- which means only push to back,
peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively.

You may simulate a queue by using a list or deque (double-ended queue),
as long as you use only standard operations of a queue.

You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if self.q1:
            self.q1.append(x)
        else:
            self.q2.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.q1:
            while len(self.q1) > 1:
                self.q2.append(self.q1.pop(0))
            return self.q1.pop(0)
        else:
            while len(self.q2) > 1:
                self.q1.append(self.q2.pop(0))
            return self.q2.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.q1:
            return self.q1[-1]
        else:
            return self.q2[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return False if self.q1 or self.q2 else True
