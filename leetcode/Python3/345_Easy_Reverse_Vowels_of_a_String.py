"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        # Create a set to hold vowels for o(1) lookups
        vowels = set("aeiouAEIOU")
        
        # Initialize left and right points `left` and `right` to equal `0` and `len(s)-1`
        left, right = 0, len(s)-1
        
        # Convert `s` to a list so we can swap characters (strings don't allow index assignment)
        s = list(s)

        # Iterate while `left` is less than `right` (traverse from left and right towards center)
        while left < right:
            # If the character at index `left` isn't in `vowels`, move right one space
            if s[left] not in vowels:
                left+=1
            # If the character at index `right` isn't in `vowels`, move left one space
            elif s[right] not in vowels:
                right-=1
            # Since both index `left` and `right` have vowels, swap them and keep advancing to center
            else:
                s[left], s[right] = s[right], s[left]
                left+=1
                right-=1
        # Join the list as a string and return the answer
        return ''.join(s)
    
sol = Solution()        
s = "IceCreAm"
print(sol.reverseVowels(s))
s = "leetcode"
print(sol.reverseVowels(s))
