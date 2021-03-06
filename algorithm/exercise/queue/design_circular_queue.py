"""
LeetCode-622

Design your implementation of the circular queue.
The circular queue is a linear data structure in which the operations are performed
based on FIFO (First In First Out) principle and the last position is connected
back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue.
In a normal queue, once the queue becomes full, we cannot insert the next element even if
there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.


Example:

MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be 3
circularQueue.enQueue(1);  // return true
circularQueue.enQueue(2);  // return true
circularQueue.enQueue(3);  // return true
circularQueue.enQueue(4);  // return false, the queue is full
circularQueue.Rear();  // return 3
circularQueue.isFull();  // return true
circularQueue.deQueue();  // return true
circularQueue.enQueue(4);  // return true
circularQueue.Rear();  // return 4

Note:

All values will be in the range of [0, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in Queue library.
"""


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
