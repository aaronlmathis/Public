"""
A sentence is a string of single-space separated words where each word consists only of lowercase letters.
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

Example 1:
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]

Explanation:
The word "sweet" appears only in s1, while the word "sour" appears only in s2.

Example 2:
Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]
"""
from typing import List
from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans = []
        s = s1.split(" ") + s2.split(" ")

        s_count = Counter(s)

        return [word for word,count in s_count.items() if count == 1]

sol = Solution()
s1 = "this apple is sweet" 
s2 = "this apple is sour" 
print(sol.uncommonFromSentences(s1, s2))