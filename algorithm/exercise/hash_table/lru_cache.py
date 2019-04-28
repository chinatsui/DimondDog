"""
LeetCode-146

Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, 
it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


class Node:

    def __init__(self, key, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self._elevate(node)
            return node.val

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self._elevate(node)
            node.val = value
        else:
            if len(self.cache) == self.capacity:
                last = self._remove_last()
                del self.cache[last.key]
            node = Node(key, value)
            self._add_to_head(node)
            self.cache[key] = node

    def _elevate(self, node):
        n_prev = node.prev
        n_next = node.next
        n_prev.next = n_next
        n_next.prev = n_prev

        h_next = self.head.next
        node.next = h_next
        h_next.prev = node
        self.head.next = node
        node.prev = self.head

    def _add_to_head(self, node):
        h_next = self.head.next
        node.next = h_next
        h_next.prev = node
        self.head.next = node
        node.prev = self.head

    def _remove_last(self):
        t_prev = self.tail.prev
        new_t_prev = t_prev.prev
        new_t_prev.next = self.tail
        self.tail.prev = new_t_prev
        return t_prev


t_cache = LRUCache(2)
t_cache.put(2, 1)
t_cache.put(2, 2)
print(t_cache.get(1))
t_cache.put(3, 3)
print(t_cache.get(2))
t_cache.put(4, 4)
print(t_cache.get(1))
print(t_cache.get(3))
print(t_cache.get(4))
