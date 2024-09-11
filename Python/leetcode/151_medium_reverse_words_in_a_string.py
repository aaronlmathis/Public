"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        words = [word for word in s.split()]
        words.reverse()
        return ' '.join(words)



sol = Solution()
s = "the sky is blue"
print(sol.reverseWords(s)) #Output: "blue is sky the"