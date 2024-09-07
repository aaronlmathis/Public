"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

"""
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        normalized = [tuple(sorted(s)) for s in strs]
        res = []
        d = {}
        for i in range(len(normalized)):
            if normalized[i] not in d:
                d[normalized[i]] = []
                d[normalized[i]].append(strs[i])
            else:
                d[normalized[i]].append(strs[i])
        for k,v in d.items():
            res.append(v)
        return res

        print(normalized)
strs = ["eat","tea","tan","ate","nat","bat"]
sol = Solution()
print(sol.groupAnagrams(strs))