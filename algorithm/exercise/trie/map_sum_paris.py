"""
LeetCode-677

Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer).
The string represents the key and the integer represents the value.
If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix,
and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
"""


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = dict()
        self.root = TrieNode('')

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.map[key] = val
        cur = self.root
        for ch in key:
            if ch in cur.des:
                cur = cur.des[ch]
            else:
                node = TrieNode(cur.s + ch)
                cur.des[ch] = node
                cur = node
        cur.is_word = True

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        cur = self.root
        for ch in prefix:
            if ch not in cur.des:
                return 0
            else:
                cur = cur.des[ch]

        q = [cur]
        sum = 0
        while q:
            node = q.pop(0)
            if node.is_word:
                sum += self.map[node.s]
            for (ch, child_node) in node.des.items():
                q.append(child_node)
        return sum


class TrieNode:

    def __init__(self, s):
        self.s = s
        self.is_word = False
        self.des = dict()

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
