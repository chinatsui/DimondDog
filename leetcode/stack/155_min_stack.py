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
        cur_min = x if cur_min is None else min(cur_min, x)
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
