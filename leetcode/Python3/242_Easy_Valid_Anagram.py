"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(t) == len(s) and all(s.count(c) == t.count(c) for c in set(s))

s = "anagram"
t = "nagaram"
sol = Solution()
print(sol.isAnagram(s, t))