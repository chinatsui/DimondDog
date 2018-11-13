class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for ch in word:
            if ch in cur.des:
                cur = cur.des[ch]
            else:
                node = TrieNode(ch)
                cur.des[ch] = node
                cur = node
        cur.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for ch in word:
            if ch in cur.des:
                cur = cur.des[ch]
            else:
                return False
        return cur.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for ch in prefix:
            if ch in cur.des:
                cur = cur.des[ch]
            else:
                return False
        return True


class TrieNode:

    def __init__(self, s):
        self.s = s
        self.is_word = False
        self.des = dict()

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
