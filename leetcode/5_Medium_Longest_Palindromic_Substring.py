"""
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right +=1
            return s[left+1:right]
        longest = ""

        for i in range(len(s)):
            odd = expand(i, i)
            if len(odd) > len(longest):
                longest = odd
            
            even = expand(i, i+1)
            if len(even) > len(longest):
                longest = even
        
        return longest


        
s = "babad"
sol = Solution()
print(sol.longestPalindrome(s))