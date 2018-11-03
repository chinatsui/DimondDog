class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_1 = []  # used for enqueue
        self.stack_2 = []  # used for dequeue

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())
        self.stack_1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        return self.stack_2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack_1:
            return self.stack_1[0]
        else:
            return self.stack_2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return False if self.stack_1 or self.stack_2 else True
