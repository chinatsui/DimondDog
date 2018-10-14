class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index >= self.size:
            return -1

        cur = self.head
        for i in range(1, index + 1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        if self.size == 0:
            self.head = ListNode(val)
        else:
            cur = ListNode(val)
            cur.next = self.head
            self.head = cur
        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        if self.size == 0:
            self.head = ListNode(val)
        else:
            cur = self.head
            for i in range(1, self.size):
                cur = cur.next
            cur.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index > self.size or index < 0:
            return

        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            prev = self.head
            for i in range(1, index):
                prev = prev.next
            cur = ListNode(val)
            cur.next = prev.next
            prev.next = cur
            self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index >= self.size or index < 0:
            return

        if index == 0:
            self.head = self.head.next
        else:
            prev = self.head
            for i in range(1, index):
                prev = prev.next
            prev.next = prev.next.next
        self.size -= 1
