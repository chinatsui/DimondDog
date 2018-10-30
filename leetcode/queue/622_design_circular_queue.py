class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.arr = [None] * k
        self.head = -1
        self.tail = -1

    def en_queue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.is_full():
            return False
        else:
            if self.head == -1 and self.tail == -1:
                self.head = 0
                self.tail = 0
                self.arr[self.tail] = value
            else:
                self.tail += 1
                self.arr[self.tail % len(self.arr)] = value
            return True

    def de_queue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.is_empty():
            return False
        else:
            self.head += 1
            return True

    def front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.is_empty():
            return -1
        else:
            return self.arr[self.head % len(self.arr)]

    def rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.is_empty():
            return -1
        else:
            return self.arr[self.tail % len(self.arr)]

    def is_empty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return True if self.head == -1 and self.tail == -1 or self.head > self.tail else False

    def is_full(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return True if self.tail - self.head + 1 == len(self.arr) else False


circularQueue = MyCircularQueue(3)
print(circularQueue.en_queue(1))
print(circularQueue.en_queue(2))
print(circularQueue.en_queue(3))
print(circularQueue.en_queue(4))
print(circularQueue.rear())
print(circularQueue.is_full())
print(circularQueue.de_queue())
print(circularQueue.en_queue(4))
print(circularQueue.rear())
