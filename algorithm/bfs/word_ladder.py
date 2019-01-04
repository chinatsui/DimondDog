"""
LeetCode-127
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.


Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.


Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
from collections import deque


class Solution:
    def ladder_length(self, beginWord, endWord, wordList):
        queue = deque()
        visited = set()
        wordSet = set(wordList)

        queue.append((beginWord, 1))
        visited.add(beginWord)

        while queue:
            word, dist = queue.popleft()
            for i in range(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    tmp = word[:i] + j + word[i+1:]
                    if tmp not in visited and tmp in wordSet:
                        if tmp == endWord:
                            return dist + 1
                        else:
                            queue.append((tmp, dist+1))
                            visited.add(tmp)
        return 0


t_word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
print(Solution().ladder_length('hit', 'cog', t_word_list))
