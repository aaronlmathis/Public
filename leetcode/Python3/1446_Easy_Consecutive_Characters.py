"""
The power of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string s, return the power of s.

Example 1:
Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:
Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Constraints:
1 <= s.length <= 500
s consists of only lowercase English letters.

"""
class Solution:
    def maxPower(self, s: str) -> int:
        left, right = 0,0
        max_count = 1
        for right in range(len(s)):
            if s[right] != s[left]:
                max_count = max(right-left, max_count)
                left=right
        max_count = max(right-left+1, max_count)
        return max_count
                
sol = Solution()

#s= ""
s = "a"
#s = "leetcode"
s = 'aaaccccc'
#s = "abbcccddddeeeeedcba"
print(sol.maxPower(s))