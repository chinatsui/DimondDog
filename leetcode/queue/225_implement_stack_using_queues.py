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
