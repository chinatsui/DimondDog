"""
LeetCode-127

Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to endWord, such that:
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


class Solution:
    @staticmethod
    def ladder_length(begin_word, end_word, word_list):
        ch_map = [set() for _ in begin_word]
        for i in range(len(begin_word)):
            for word in word_list:
                ch_map[i].add(word[i])

        word_set = set(word_list)
        q, dist, visited = [begin_word], 1, {begin_word}
        while q:
            tmp = []
            for word in q:
                for i in range(len(word)):
                    for ch in ch_map[i]:
                        if word[i] == ch:
                            continue

                        transformed = word[0:i] + ch + word[i + 1:]
                        if transformed in visited or transformed not in word_set:
                            continue
                        elif transformed == end_word:
                            return dist + 1
                        else:
                            visited.add(transformed)
                            tmp.append(transformed)
            dist += 1
            q = tmp
        return 0


t_word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
print(Solution().ladder_length('hit', 'cog', t_word_list))
