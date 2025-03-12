"""
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

Example 3:
Input: s = "abc"
Output: 1
 
Constraints:
3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
"""
from collections import Counter

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        char_count = Counter()
        substring_count = 0
        left = 0

        for right in range(len(s)):
            curr_char = s[right]
            char_count[curr_char]+=1

            while len(char_count) == 3:
                char_left = s[left]
                char_count[char_left]-=1
                if char_count[char_left] == 0:
                    del char_count[char_left]
                
                left+=1
            substring_count += left
        return substring_count



sol = Solution()
s = "abcabc"
print(f"{sol.numberOfSubstrings(s)} Expected: 10")
s = "aaacb"
print(f"{sol.numberOfSubstrings(s)} Expected: 3")
s = "abc"
print(f"{sol.numberOfSubstrings(s)} Expected: 1")