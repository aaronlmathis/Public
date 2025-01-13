"""
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

Example 1:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]

Example 2:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]

Constraints:
1 <= words1.length, words2.length <= 104
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
"""
from typing import List
from collections import defaultdict, Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Create set of words1 for quick retrieval
        ans = set(words1)

        # Create hashmap for tracking character counts
        chars = {}

        # Iterate through subsets in words2, then iterate through characters in subset
        for sub in words2:
            for char in sub:
                # Take count of character freq in subset. If character is not in hashmap or the count is greater
                # Add it to frequency count hasmap. This gets us the maximum frequency of a character in all subsets
                count = sub.count(char)
                if char not in chars or count > chars[char]:
                    chars[char] = count
        # Iterate through words in words1, for every character in frequency hashmap, check if character appears less
        # in word than it does in any of the subsets. If so, remove it from answer set.
        for word in words1:
            for char in chars:
                if word.count(char) < chars[char]:
                    ans.remove(word)
                    break
        # return answer as a list
        return list(ans)

sol = Solution()
words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]        
print(sol.wordSubsets(words1, words2))