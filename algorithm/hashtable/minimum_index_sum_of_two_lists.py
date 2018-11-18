"""
LeetCode-599

Suppose Andy and Doris want to choose a restaurant for dinner,
and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum.
If there is a choice tie between answers, output all of them with no order requirement.
You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
"""


class Solution:
    @staticmethod
    def find_restaurant(list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res = []
        idx_sum = -1
        name_idx_map1 = {name: idx for (idx, name) in enumerate(list1)}
        for (i, n) in enumerate(list2):
            if n in name_idx_map1:
                cur_idx_sum = i + name_idx_map1[n]
                if idx_sum == -1:
                    idx_sum = cur_idx_sum
                    res.append(n)
                elif idx_sum == cur_idx_sum:
                    res.append(n)
                elif idx_sum > cur_idx_sum:
                    idx_sum = cur_idx_sum
                    res.clear()
                    res.append(n)
        return res
