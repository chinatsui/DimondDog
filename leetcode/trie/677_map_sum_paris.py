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
