"""
Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 
"""
from collections import Counter
class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        
        if len1 > len2:
            return False
        
        # Create frequency counters for s1 and for the first window in s2
        s1_count = Counter(s1)
        window_count = Counter(s2[:len1])
        
        if s1_count == window_count:
            return True
        
        # Sliding window over s2
        for i in range(len1, len2):
            # Add the next character to the window
            window_count[s2[i]] += 1
            # Remove the character that is no longer in the window
            window_count[s2[i - len1]] -= 1
            
            # Remove the count of the character if it drops to 0 to keep the counters clean
            if window_count[s2[i - len1]] == 0:
                del window_count[s2[i - len1]]
            
            # Check if the current window matches the s1 frequency count
            if s1_count == window_count:
                return True
        
        return False

sol=Solution()
s1 = "ab"
s2 = "eidboaoo"
print(sol.checkInclusion(s1, s2))